---
description: Запустить Deep Research для курса (Perplexity)
allowed-tools: Read, Write, Edit, Bash, AskUserQuestion
---

# /course-research — Deep Research

Запусти Stage 02 (Deep Research) для курса.

## Инструкции

1. Прочитай инструкции стейджа: `.claude/skills/content-pipeline/stages/02-research.md`
2. Следуй инструкциям стейджа

Если пользователь указал slug курса в аргументах ($ARGUMENTS) — используй его.

Если нет — найди курсы в `courses/` и спроси для какого запускать.

Входные данные: $ARGUMENTS
