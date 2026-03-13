---
name: content-pipeline
description: "AI Content Generation Pipeline для курсов OSNOVA. Используй когда нужно: (1) создать новый курс от идеи, (2) сгенерировать контент через pipeline, (3) возобновить paused pipeline."
---

# Content Pipeline — Оркестратор

Пошаговый pipeline создания курсов: Идея -> Bootstrap -> Research -> PRD -> [Review] -> Структура -> [Review] -> Content -> Tests -> Translation.

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

  ✅ 01 Bootstrap
  ✅ 02 Deep Research
  🔄 03 PRD                ◄ текущий этап
  ⬜ 04 Structure
  ⬜ 05 Module Research
  ⬜ 06 Content Generation     (Sprint 2)
  ⬜ 07 Tests                  (Sprint 2)
  ⬜ 08 Translation            (Sprint 2)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

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
2. Создай папку `courses/{slug}/`
3. Создай `pipeline-state.json`:

```json
{
  "course_slug": "{slug}",
  "current_stage": "01-bootstrap",
  "created_at": "{ISO datetime}",
  "stages": {}
}
```

4. Перейди к Stage 01

### Возобновление

Если пользователь просит продолжить:

1. Прочитай `pipeline-state.json` из указанной или найденной папки курса
2. Определи `current_stage`
3. Если статус `review_pending` — покажи артефакт и спроси решение (Утвердить / Правки / Отклонить)
4. Перейди к соответствующему stage

## Порядок стейджей

| # | Stage | Human Gate | Sprint |
|---|-------|-----------|--------|
| 01 | Bootstrap | - | 1 |
| 02 | Deep Research | - | 1 |
| 03 | PRD | Gate 1: PRD Review | 1 |
| 04 | Structure | Gate 2: Методолог Review | 1 |
| 05 | Module Research | - | 2 |
| 06 | Content Generation | - | 2 |
| 07 | Tests | - | 2 |
| 08 | Translation | - | 2 |

## Выполнение стейджа

Для каждого стейджа:

1. Прочитай инструкции из `.claude/skills/content-pipeline/stages/{nn}-{name}.md`
2. Выполни инструкции стейджа
3. Сохрани результат в папку курса
4. Обнови `pipeline-state.json`:

```json
{
  "stages": {
    "{stage_id}": {
      "status": "completed",
      "completed_at": "{ISO datetime}"
    }
  },
  "current_stage": "{next_stage_id}"
}
```

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
