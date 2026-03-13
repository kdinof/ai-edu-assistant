---
description: Сгенерировать структуру курса из PRD
allowed-tools: Read, Write, Edit, AskUserQuestion
---

# /course-structure — Генерация структуры курса

Запусти Stage 04 (Structure) для курса.

## Инструкции

1. Прочитай инструкции стейджа: `.claude/skills/content-pipeline/stages/04-structure.md`
2. Следуй инструкциям стейджа

Если пользователь указал slug курса в аргументах ($ARGUMENTS) — используй его.

Если нет — найди курсы в `courses/` и спроси для какого запускать.

Входные данные: $ARGUMENTS
