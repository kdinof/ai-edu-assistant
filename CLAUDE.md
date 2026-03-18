# AI Content Pipeline

AI-пайплайн для автоматизации создания курсов OSNOVA.

## Pipeline

```
Идея → Bootstrap → Deep Research → PRD → [Human Review] →
→ Структура → [Методолог Review] → Модульный Research →
→ Content Generation → [Validation] → Тесты → Lesson Summaries → Перевод (RU/UZ)
```

## Структура проекта

```
.claude/
├── commands/                    # Slash-команды
├── skills/
│   ├── content-pipeline/        # Skill: оркестратор + stages + templates
│   │   ├── knowledge-base/      # Как добавлять reference-курсы
│   │   ├── references/          # Pipeline stages, quality gates
│   │   ├── stages/              # Инструкции для каждого этапа
│   │   └── templates/           # Шаблоны артефактов
│   ├── fact-check/              # Верификация технических утверждений
│   └── perplexity-research/     # Perplexity API скрипты (Stage 02)

courses/                         # Результаты pipeline
└── claude-cowork-office/        # Курс: Claude Cowork Office
    ├── _archive/
    ├── 05-module-research/
    ├── 06-content/
    └── research-aspects/

foundation/                      # Долгосрочные reference-файлы
```

## Reference файлы

| Файл | Назначение |
|------|-----------|
| `foundation/course-design-values.md` | Ценности курсов (Stage 03) |
| `foundation/brand_tone_of_voice.md` | Tone of voice (Stage 06) |
| `.claude/skills/perplexity-research/` | Perplexity API скрипты (Stage 02) |

## Запуск

```bash
cd projects/active/ai-edu-assistant
claude
# затем: /pipeline
```

## Communication Style

Отвечай на русском. Короткие, точные ответы. Делай только то, что запрошено.
