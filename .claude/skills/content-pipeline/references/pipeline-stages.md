# Pipeline Stages — Контракты вход/выход

## Stage 01: Bootstrap

- **ID:** `01-bootstrap`
- **Вход:** Идея курса (свободный текст от пользователя)
- **Выход:** `01-bootstrap.md` — заполненный опросник + заполненная `references/` (обязательно)
- **Инструкции:** `stages/01-bootstrap.md`
- **Шаблон:** `templates/bootstrap-questionnaire.md`
- **Human Gate:** Нет

## Stage 02: PRD

- **ID:** `02-prd`
- **Вход:** `01-bootstrap.md` + `references/*`
- **Выход:** `02-prd.md`
- **Инструкции:** `stages/02-prd.md`
- **Шаблон:** `templates/prd.md`
- **Human Gate:** Gate 1 — PRD Review (Утвердить / Правки / Отклонить)

## Stage 03: Structure

- **ID:** `03-structure`
- **Вход:** `02-prd.md` (approved) + `references/*`
- **Выход:** `03-structure.md`
- **Инструкции:** `stages/03-structure.md`
- **Шаблон:** `templates/course-structure.md`
- **Human Gate:** Gate 2 — Методолог Review (Утвердить / Правки / Отклонить)

## Stage 04: Content Generation

- **ID:** `04-content`
- **Вход:** `03-structure.md` (approved) + `references/*`
- **Выход:** `04-content/module-{nn}/lesson-{nn}.md`
- **Инструкции:** `stages/04-content.md`
- **Шаблон:** `templates/lesson.md`
- **Human Gate:** Нет

## Stage 05: Tests

- **ID:** `05-tests`
- **Вход:** `03-structure.md` (learning outcomes) + `04-content/module-{nn}/lesson-{nn}.md`
- **Выход:** `05-tests/module-{nn}/lesson-{nn}-test.md` — тест к каждому уроку
- **Инструкции:** `stages/05-tests.md`
- **Шаблон:** `templates/test.md`
- **Параметры:** 3-5 вопросов на урок, проходной балл 70%
- **Типы вопросов:** single_choice, multiple_choice, scenario, find_error
- **Human Gate:** Нет

## Stage 06: Lesson Summaries

- **ID:** `06-lesson-summaries`
- **Вход:** `04-content/module-{nn}/lesson-{nn}.md` — контент уроков
- **Выход:** `04-content/module-{nn}/lesson-{nn}_summary.md` — текстовые описания (рекапы) к каждому уроку, рядом с уроком
- **Инструкции:** `stages/06-lesson-summaries.md`
- **Агент:** `lesson-summary-writer`
- **Human Gate:** Нет

## Stage 07: Translation (опционально)

- **ID:** `07-translation`
- **Вход:** Артефакты stages 03-06 + целевые языки курса
- **Выход:** `07-translations/{lang}/`
- **Инструкции:** `stages/07-translation.md`
- **Human Gate:** Нет

---

## Pipeline State Schema

```json
{
  "course_slug": "string",
  "current_stage": "string (stage ID)",
  "created_at": "ISO 8601 datetime",
  "has_references": "boolean (always true after bootstrap — references are mandatory)",
  "references": {
    "files_count": "number (optional)",
    "links_count": "number (optional)"
  },
  "stages": {
    "{stage_id}": {
      "status": "pending | in_progress | completed | approved | review_pending | revision | rejected",
      "started_at": "ISO 8601 datetime",
      "completed_at": "ISO 8601 datetime (optional)",
      "feedback": "string (optional, user feedback for revisions)",
      "tokens": "number (total tokens used by this stage)",
      "tokens_estimated": "boolean (optional, true if tokens are approximate)"
    }
  }
}
```

### Статусы

| Статус | Описание |
|--------|----------|
| `pending` | Стейдж ожидает выполнения |
| `in_progress` | Стейдж выполняется |
| `completed` | Стейдж завершён (без human gate) |
| `review_pending` | Ожидает ревью человека |
| `approved` | Одобрено человеком |
| `revision` | Отправлено на доработку |
| `rejected` | Отклонено |
