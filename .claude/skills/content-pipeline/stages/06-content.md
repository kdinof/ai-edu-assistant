# Stage 06: Content Generation (Sprint 2)

## Задача

Сгенерировать контент для каждого урока: видео-скрипт + текст + ключевые выводы.

## Вход
- `04-structure.md` + `05-module-research/`

## Выход
- `06-content/module-{nn}/lesson-{nn}.md`

## Подход
1. Последовательно по модулям
2. Для каждого урока использовать шаблон `templates/lesson.md`
3. Reference: `foundation/brand_tone_of_voice.md`

## Post-step: Fact-Check

После генерации каждого модуля **автоматически** запускай skill `fact-check` в фоне:
- Используй Agent tool с `run_in_background: true`
- Передай путь к сгенерированному модулю: `courses/{slug}/06-content/module-{NN}/`
- Результат сохраняется в `fact-check-report.md` внутри папки модуля
- Не жди завершения — продолжай работу или спрашивай пользователя о следующем шаге
