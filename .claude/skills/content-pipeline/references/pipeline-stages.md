# Pipeline Stages — Контракты вход/выход

## Stage 01: Bootstrap

- **ID:** `01-bootstrap`
- **Вход:** Идея курса (свободный текст от пользователя)
- **Выход:** `01-bootstrap.md` — заполненный опросник
- **Инструкции:** `stages/01-bootstrap.md`
- **Шаблон:** `templates/bootstrap-questionnaire.md`
- **Human Gate:** Нет

## Stage 02: Deep Research

- **ID:** `02-research`
- **Вход:** `01-bootstrap.md`
- **Выход:** `02-research.md` — многоаспектный отчёт с синтезом и quality assessment
- **Инструкции:** `stages/02-research.md`
- **Шаблон:** `templates/research-report.md`
- **Зависимости:** Perplexity API (`.claude/skills/perplexity-research/research.py`), параллельные Task() субагенты (один на аспект)
- **Human Gate:** Нет (автоматический quality gate: PASS/WARN/FAIL)
- **Metadata в state:** `aspects_count`, `sources_count`, `quality_verdict`

## Stage 03: PRD

- **ID:** `03-prd`
- **Вход:** `01-bootstrap.md` + `02-research.md`
- **Выход:** `03-prd.md`
- **Инструкции:** `stages/03-prd.md`
- **Шаблон:** `templates/prd.md`
- **Reference:** `foundation/course-design-values.md`
- **Human Gate:** Gate 1 — PRD Review (Утвердить / Правки / Отклонить)

## Stage 04: Structure

- **ID:** `04-structure`
- **Вход:** `03-prd.md` (approved) + `02-research.md`
- **Выход:** `04-structure.md`
- **Инструкции:** `stages/04-structure.md`
- **Шаблон:** `templates/course-structure.md`
- **Reference формат:** шаблон `templates/course-structure.md`
- **Human Gate:** Gate 2 — Методолог Review (Утвердить / Правки / Отклонить)

## Stage 05: Module Research (Sprint 2)

- **ID:** `05-module-research`
- **Вход:** `04-structure.md` (approved)
- **Выход:** `05-module-research/module-{nn}.md`
- **Инструкции:** `stages/05-module-research.md`
- **Зависимости:** Perplexity API, параллельные Agent subagents

## Stage 06: Content Generation (Sprint 2)

- **ID:** `06-content`
- **Вход:** `04-structure.md` + `05-module-research/`
- **Выход:** `06-content/module-{nn}/lesson-{nn}.md`
- **Инструкции:** `stages/06-content.md`
- **Шаблон:** `templates/lesson.md`
- **Reference:** `foundation/brand_tone_of_voice.md`

## Stage 07: Tests (Sprint 2)

- **ID:** `07-tests`
- **Вход:** `06-content/`
- **Выход:** `07-tests/module-{nn}-test.md`
- **Инструкции:** `stages/07-tests.md`
- **Шаблон:** `templates/test.md`

## Stage 08: Translation (Sprint 2)

- **ID:** `08-translation`
- **Вход:** Все файлы stages 04-07
- **Выход:** `08-translations/uz/`
- **Инструкции:** `stages/08-translation.md`

---

## Pipeline State Schema

```json
{
  "course_slug": "string",
  "current_stage": "string (stage ID)",
  "created_at": "ISO 8601 datetime",
  "stages": {
    "{stage_id}": {
      "status": "pending | in_progress | completed | approved | review_pending | revision | rejected",
      "started_at": "ISO 8601 datetime",
      "completed_at": "ISO 8601 datetime (optional)",
      "feedback": "string (optional, user feedback for revisions)"
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
