---
description: Запуск или возобновление Content Pipeline для создания курса
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Agent, AskUserQuestion
---

# /pipeline — Content Pipeline

Запусти или возобнови Content Pipeline для создания курса.

## Инструкции

1. Прочитай оркестратор: `.claude/skills/content-pipeline/SKILL.md`
2. Следуй его инструкциям

### Новый курс

Если пользователь предоставил идею курса в аргументах команды ($ARGUMENTS):
- Используй её как входные данные для Stage 01 (Bootstrap)
- Спроси slug для курса

Если аргументов нет:
- Спроси пользователя: "Опиши идею курса" или "Укажи slug существующего курса для возобновления"

### Возобновление

Если пользователь указал slug существующего курса:
- Найди `courses/{slug}/pipeline-state.json`
- Определи текущий стейдж и продолжи

Входные данные: $ARGUMENTS
