---
description: Сгенерировать тесты для уроков модуля
allowed-tools: Read, Write, Edit, Glob, AskUserQuestion
---

# /lesson-tests — Генерация тестов для уроков

Запусти Stage 07 (Tests) для конкретного модуля курса.

## Инструкции

1. Прочитай инструкции стейджа: `.claude/skills/content-pipeline/stages/07-tests.md`
2. Следуй инструкциям стейджа

## Аргументы

Формат: `{course-slug} module-{nn}` или `{course-slug}` или без аргументов.

Примеры:
- `/lesson-tests claude-cowork-office module-01` — тесты для модуля 1
- `/lesson-tests claude-cowork-office` — спросить какой модуль
- `/lesson-tests` — спросить какой курс и модуль

Если пользователь указал slug и модуль в аргументах ($ARGUMENTS) — используй их.

Если указан только slug — найди модули в `courses/{slug}/06-content/` и спроси для какого модуля генерировать.

Если аргументов нет — найди курсы в `courses/` и спроси для какого курса и модуля запускать.

**Не обновляй pipeline-state.json** — эта команда работает независимо от pipeline.

Входные данные: $ARGUMENTS
