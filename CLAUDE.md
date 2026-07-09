# AI Content Pipeline

AI-пайплайн для автоматизации создания образовательных курсов.

## Pipeline

```
Идея → Bootstrap (+референсы) → PRD → [Human Review] →
→ Структура → [Методолог Review] →
→ Content Generation → [Validation] → Тесты → Lesson Summaries → Перевод (опционально)
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
│   └── fact-check/              # Верификация технических утверждений

courses/                         # Результаты pipeline
└── claude-cowork-office/        # Курс: Claude Cowork Office
    ├── _archive/
    ├── 05-module-research/
    ├── 06-content/
    └── research-aspects/
```

## Запуск

```bash
cd projects/active/ai-edu-assistant
claude
# затем: /pipeline
```

## Communication Style

Отвечай на русском. Короткие, точные ответы. Делай только то, что запрошено.
