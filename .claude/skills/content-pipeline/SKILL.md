---
name: content-pipeline
description: "AI Content Generation Pipeline для образовательных курсов. Используй когда нужно: (1) создать новый курс от идеи, (2) сгенерировать контент через pipeline, (3) возобновить paused pipeline."
---

# Content Pipeline — Оркестратор

Пошаговый pipeline создания курсов: Идея -> Bootstrap (+референсы) -> PRD -> [Review] -> Структура -> [Review] -> Content -> Tests -> Lesson Summaries -> Translation (опционально).

## Как работает

1. Читает `pipeline-state.json` из папки курса
2. Определяет текущий стейдж
3. **Показывает Roadmap** (текущее состояние pipeline)
4. Делегирует выполнение в `stages/{nn}-{name}.md`
5. Сохраняет результат в папку курса
6. Обновляет `pipeline-state.json`

## Roadmap — визуальная карта прогресса

**При старте и при завершении каждого стейджа** выводи Roadmap в формате:

```
━━━ CONTENT PIPELINE: {course_slug} ━━━

  ✅ 01 Bootstrap              12.5K tokens
  🔄 02 PRD                ◄ текущий этап
  ⬜ 03 Structure
  ⬜ 04 Content Generation
  ⬜ 05 Tests
  ⬜ 06 Lesson Summaries
  ⬜ 07 Translation

  ──────────────────────────────────
  Потрачено: 12.5K tokens · ~$0.19
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Токены и стоимость:**
- Для каждого завершённого стейджа показывай количество токенов (из `pipeline-state.json`)
- Внизу — сумму по всем завершённым стейджам и примерную стоимость
- Стоимость рассчитывай по формуле: `tokens * $15 / 1_000_000` (средняя цена input token Claude Opus)
- Это приблизительная оценка — реальная стоимость зависит от соотношения input/output токенов

**Статусы:**
- `✅` — completed / approved
- `🔄` — in_progress (текущий)
- `⏳` — review_pending (ждёт решения пользователя)
- `🔁` — revision (на доработке)
- `❌` — rejected
- `⬜` — pending (ещё не начат)

Определяй статусы из `pipeline-state.json`. Для текущего стейджа всегда ставь `🔄` (или `⏳` если review_pending).

## Запуск

### Новый курс

Если пользователь предоставил идею курса:

1. Спроси slug для курса (латиница, kebab-case). Пример: `ai-visual-creator`
2. Создай папку `courses/{slug}/` и подпапку `courses/{slug}/references/`
3. Создай `pipeline-state.json`:

```json
{
  "course_slug": "{slug}",
  "current_stage": "01-bootstrap",
  "created_at": "{ISO datetime}",
  "has_references": false,
  "stages": {}
}
```

4. Перейди к Stage 01. **Папка `references/` обязательна**: Stage 01 (Bootstrap) не считается завершённым, пока пользователь не загрузит туда хотя бы один файл (или ссылки в `references/links.md`) — без референсов pipeline дальше не идёт

### Возобновление

Если пользователь просит продолжить:

1. Прочитай `pipeline-state.json` из указанной или найденной папки курса
2. Определи `current_stage`
3. Если статус `review_pending` — покажи артефакт и спроси решение (Утвердить / Правки / Отклонить)
4. Перейди к соответствующему stage

### Курсы со старой нумерацией стейджей

Если `current_stage` в `pipeline-state.json` использует старый ID (курс создан до перенумерации), примени мэппинг:

| Старый ID | Что делать |
|-----------|-----------|
| `02-research` | Research удалён из pipeline. Если референсы уже загружены — продолжай с `02-prd`. Если референсов нет — вернись к `01-bootstrap` за референсами |
| `03-prd` | Продолжай как `02-prd` |
| `04-structure` | Продолжай как `03-structure` |
| `05-module-research` | Module Research удалён. Продолжай с `04-content` |
| `06-content` | Продолжай как `04-content` |
| `07-tests` | Продолжай как `05-tests` |
| `08-lesson-summaries` | Продолжай как `06-lesson-summaries` |
| `09-translation` | Продолжай как `07-translation` |

**Важно:** артефакты старых курсов лежат по старым путям и именам файлов (`03-prd.md`, `04-structure.md`, `06-content/`, `07-tests/`, `08-translations/` и т.д.) — при возобновлении читай их по этим старым именам, не переименовывай задним числом.

## Порядок стейджей

| # | Stage | Human Gate |
|---|-------|-----------|
| 01 | Bootstrap | - |
| 02 | PRD | Gate 1: PRD Review |
| 03 | Structure | Gate 2: Методолог Review |
| 04 | Content Generation | - |
| 05 | Tests | - |
| 06 | Lesson Summaries | - |
| 07 | Translation (опционально) | - |

## Выполнение стейджа

Для каждого стейджа:

1. Прочитай инструкции из `.claude/skills/content-pipeline/stages/{nn}-{name}.md`
2. Выполни инструкции стейджа
3. Сохрани результат в папку курса
4. Обнови `pipeline-state.json` (включая токены):

```json
{
  "stages": {
    "{stage_id}": {
      "status": "completed",
      "completed_at": "{ISO datetime}",
      "tokens": 45200
    }
  },
  "current_stage": "{next_stage_id}"
}
```

## Трекинг токенов

После завершения каждого стейджа записывай количество использованных токенов в поле `tokens`:

- **Agent subagents** (translation, fact-check): бери `total_tokens` из результата Agent tool
- **Основной контекст** (bootstrap, PRD, structure, content, tests): оцени приблизительно — сумма токенов всех прочитанных файлов + сгенерированного контента. Для оценки: 1 слово ~ 1.3 токена
- Если точное число недоступно — запиши приблизительную оценку и добавь `"tokens_estimated": true`

Стоимость рассчитывается при отображении Roadmap: `total_tokens * $15 / 1_000_000`

## Human Gates

При достижении human gate:

1. Установи статус стейджа: `"review_pending"`
2. Покажи пользователю сгенерированный артефакт (ключевые секции)
3. Покажи Roadmap с текущим статусом `⏳`
4. Используй **AskUserQuestion** с вариантами: `["Утвердить", "Правки", "Отклонить"]`
5. При утверждении: статус -> `"approved"`, переход к следующему стейджу
6. При правках: спроси детали через AskUserQuestion (freeform), перезапусти стейдж с фидбеком, статус -> `"revision"`
7. При отклонении: статус -> `"rejected"`, стоп

## Переходы между стейджами

При переходе (конец стейджа → начало следующего):

1. Покажи Roadmap с обновлённым статусом
2. Используй **AskUserQuestion** для подтверждения перехода. Пример:
   - question: "Продолжить к следующему этапу?"
   - options: `["Продолжить", "Остановиться"]`
3. Не используй inline текст "Спроси: перейти к X или остановиться?" — всегда AskUserQuestion

## References

- Описание стейджей: `.claude/skills/content-pipeline/references/pipeline-stages.md`
- Критерии качества: `.claude/skills/content-pipeline/references/quality-gates.md`
