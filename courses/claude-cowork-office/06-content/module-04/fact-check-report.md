# Fact-Check Report: Module 04

**Дата:** 2026-03-17
**Файлы:** lesson-01.md, lesson-02.md, lesson-03.md, lesson-04.md
**Сущностей проверено:** 13

## Результат: PASS

## Проблемы (если есть)

Критических проблем не обнаружено.

### ⚠️ Неточности

| Сущность | Урок | Проблема | Актуальная информация | Источник |
|----------|------|----------|----------------------|----------|
| python-pptx | 4.1 | Упомянута как активная библиотека, но проект практически не поддерживается | python-pptx существует на PyPI (v1.0.2), но не обновлялась более 12 месяцев. Есть активный форк python-pptx-ng. Однако Claude использует встроенный PPTX skill через code execution, а не напрямую python-pptx — упоминание библиотеки в контенте корректно как пояснение механизма | [PyPI](https://pypi.org/project/python-pptx/) |
| Подход PPTX через code execution | 4.1 | Описан как "через Python-библиотеку python-pptx" — это упрощение | Claude использует встроенный PPTX skill через систему Skills + code execution container. python-pptx используется внутри, но пользователь не взаимодействует с библиотекой напрямую. Упрощение допустимо для целевой аудитории курса | [Claude Help Center](https://support.claude.com/en/articles/13521390-use-claude-for-powerpoint) |

### ❌ Не найдено

Нет.

## ✅ Проверено и подтверждено

- **Claude Cowork / Cowork** — продукт Anthropic, запущен в research preview 12 января 2026. Описание как AI-агента для офисных задач корректно. [VentureBeat](https://venturebeat.com/orchestration/anthropic-says-claude-code-transformed-programming-now-claude-cowork-is-coming-for-the-rest-of-the-enterprise-/)
- **Google Workspace CLI (gws)** — существует, npm-пакет `@googleworkspace/cli`, написан на Rust. Аббревиатура "gws" корректна. Работает с Drive, Gmail, Calendar, Sheets, Docs, Slides. [GitHub](https://github.com/googleworkspace/cli), [npm](https://www.npmjs.com/package/@googleworkspace/cli)
- **Google Slides** — корректно упомянут как инструмент для создания презентаций через gws
- **Google Docs** — корректно упомянут как инструмент для создания отчётов через gws
- **Google Sheets** — корректно упомянут как источник данных через gws
- **Google Drive** — корректно упомянут как место хранения файлов
- **Speaker notes в Google Slides** — функция существует, поддерживается через Google Slides API. [Google Developers](https://developers.google.com/workspace/slides/api/guides/notes)
- **Skills (Claude Cowork)** — концепция skills как markdown-инструкций для Claude подтверждена. Упоминание в уроке 4.3 о модуле 5 корректно. [Claude Help Center](https://support.claude.com/en/articles/12512180-use-skills-in-claude)
- **Code execution (Claude)** — функция выполнения кода в Claude существует, используется для генерации файлов (PPTX, XLSX, DOCX). [Claude API Docs](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)
- **Пайплайн (pipeline)** — общий термин, используется корректно в контексте цепочки задач
- **Фреймворк "Что → Откуда → Куда → Формат"** — авторский фреймворк курса, ссылка на модуль 2 корректна в рамках структуры курса
