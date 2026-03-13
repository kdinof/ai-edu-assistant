# AI Content Pipeline

AI-пайплайн для автоматизации создания образовательных курсов OSNOVA — от идеи до готового контента.

## Требования

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) (CLI)
- Python 3.10+
- Ключ [Perplexity API](https://www.perplexity.ai/settings/api) (для этапов Deep Research)

## Установка

1. Клонируй репозиторий и перейди в папку проекта:

```bash
cd projects/active/ai-edu-assistant
```

2. Запусти Claude Code и попроси добавить ключ:

```bash
claude
```

```
Добавь PERPLEXITY_API_KEY=pplx-xxx в .env
```

Claude создаст файл `.env` и запишет ключ. Получить ключ: [perplexity.ai/settings/api](https://www.perplexity.ai/settings/api).

3. Проверь setup (можно попросить Claude или вручную):

```bash
python .claude/skills/perplexity-research/search.py --check-setup
```

## Запуск

```bash
claude
```

Затем используй одну из команд:

| Команда | Что делает |
|---------|-----------|
| `/pipeline` | Запуск или возобновление полного pipeline (определяет текущий этап автоматически) |
| `/bootstrap` | Только Stage 01 — интерактивный опросник для нового курса |
| `/course-research` | Только Stage 02 — deep research через Perplexity API |
| `/course-structure` | Только Stage 04 — генерация структуры курса из PRD |

## Как работает Pipeline

```
Идея → Bootstrap → Deep Research → PRD → [Human Review] →
→ Структура → [Методолог Review] → Модульный Research →
→ Content Generation → [Validation] → Тесты → Перевод (RU/UZ)
```

### Этапы

| # | Stage | Что происходит | Human Gate |
|---|-------|---------------|------------|
| 01 | **Bootstrap** | Интерактивный опросник: тема, аудитория, learning outcomes, финальный артефакт, инструменты, конкуренты | — |
| 02 | **Deep Research** | Мульти-аспектный research через Perplexity API (рынок, конкуренты, ЦА, методология, инструменты). Автоматический quality gate (PASS/WARN/FAIL) | — |
| 03 | **PRD** | Синтез bootstrap + research в Product Requirements Document | PRD Review |
| 04 | **Structure** | Детальная структура курса: модули (15-30 мин), уроки (5-10 мин), практика | Методолог Review |
| 05 | **Module Research** | Параллельный research по каждому модулю через sub-agents | — |
| 06 | **Content Generation** | Контент уроков: видео-скрипт + текст + ключевые выводы | — |
| 07 | **Tests** | Квиз-вопросы + практические задания на модуль | — |
| 08 | **Translation** | Перевод RU → UZ с сохранением markdown-структуры | — |

### Human Gates

Pipeline останавливается в двух точках для ревью:
- **После Stage 03 (PRD)** — проверка learning outcomes, скоупа, позиционирования
- **После Stage 04 (Structure)** — проверка структуры методологом

Варианты решения: Утвердить / Правки / Отклонить.

### Состояние Pipeline

Прогресс сохраняется в `courses/{slug}/pipeline-state.json`. При повторном запуске `/pipeline` — продолжает с последнего этапа.

## Структура проекта

```
.claude/
├── commands/                    # Slash-команды (/pipeline, /bootstrap, ...)
├── skills/
│   ├── content-pipeline/        # Оркестратор pipeline
│   │   ├── stages/              # Инструкции для каждого этапа
│   │   ├── templates/           # Шаблоны артефактов
│   │   ├── references/          # Контракты вход/выход, quality gates
│   │   └── knowledge-base/      # Как добавлять reference-курсы
│   ├── fact-check/              # Верификация технических утверждений
│   └── perplexity-research/     # Perplexity API скрипты

courses/                         # Результаты pipeline
└── {slug}/                      # Папка курса
    ├── pipeline-state.json
    ├── 01-bootstrap.md
    ├── 02-research.md
    ├── 03-prd.md
    ├── 04-structure.md
    ├── 05-module-research/
    └── 06-content/

foundation/                      # Долгосрочные reference-файлы
├── course-design-values.md      # Ценности курсов (Stage 03, 04)
└── brand_tone_of_voice.md       # Tone of voice (Stage 06)
```
