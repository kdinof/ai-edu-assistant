# Fact-Check Report: Module 02

**Дата:** 2026-03-11
**Файлы:** lesson-01.md, lesson-02.md, lesson-03.md, lesson-04.md
**Сущностей проверено:** 14

## Результат: ISSUES FOUND

## Проблемы

### ⚠️ Неточности

| Сущность | Урок | Проблема | Актуальная информация | Источник |
|----------|------|----------|----------------------|----------|
| `gws sheets get` | 2.2 | Неточный синтаксис команды. В уроке написано: «Cowork выполняет `gws sheets get`» | Реальный синтаксис: `gws sheets spreadsheets values get --params '{"spreadsheetId": "ID", "range": "Sheet1!A1:C10"}'`. Формат CLI: `gws <service> <resource> <method>` | [GitHub: googleworkspace/cli](https://github.com/googleworkspace/cli), [skills/gws-sheets-read](https://github.com/googleworkspace/cli/blob/main/skills/gws-sheets-read/SKILL.md) |
| `gws docs create` | 2.2 | Неточный синтаксис команды. В уроке написано: «Выполняет `gws docs create`» | Реальный синтаксис следует паттерну `gws docs documents <method>`. Для создания документа используется ресурс `documents` | [GitHub: googleworkspace/cli](https://github.com/googleworkspace/cli) |
| `gws drive` | 2.2 | Слишком упрощённый синтаксис. В уроке написано: «Сохраняет в указанную папку через `gws drive`» | Реальный синтаксис: `gws drive files <method>`, например `gws drive files list --params '{"pageSize": 10}'` или `gws drive files create --json '{"name": "Project", "mimeType": "..."}'` | [GitHub: googleworkspace/cli](https://github.com/googleworkspace/cli) |
| Cowork показывает план автоматически | 2.1, 2.2, 2.3 | В уроках описано, что Cowork «показывает план и ждёт одобрения» как поведение по умолчанию | Показ плана перед выполнением — рекомендуемая практика, но требует настройки через Global Instructions: «Show a brief plan before taking action on any task. Wait for my approval before executing.» Без этой настройки Cowork может сразу выполнять задачу | [Claude Cowork Starter Guide](https://claudiaplusai.substack.com/p/claude-cowork-starter-guide-30-examples), [Cowork Setup Guide](https://dreamsaicanbuy.com/blog/claude-cowork-setup-guide) |

### 🔍 Требует уточнения

| Сущность | Урок | Контекст использования | Комментарий |
|----------|------|----------------------|-------------|
| «Cowork берёт сам через Google Workspace CLI» | 2.1 | В таблице «Промпт vs задание» описано, что Cowork работает через Google Workspace CLI | Cowork может работать с Google через MCP-коннекторы, встроенные интеграции (Google Drive connector) или через gws CLI. Способ зависит от настройки. Утверждение, что Cowork работает исключительно через Google Workspace CLI, упрощает реальность |

## ✅ Проверено и подтверждено

- **Claude Cowork** — реальный продукт Anthropic, запущен в январе 2026 (Mac), февраль 2026 (Windows). Десктопный агент для автоматизации офисных задач. Источник: [CNBC](https://www.cnbc.com/2026/02/24/anthropic-claude-cowork-office-worker.html), [VentureBeat](https://venturebeat.com/orchestration/anthropic-says-claude-code-transformed-programming-now-claude-cowork-is-coming-for-the-rest-of-the-enterprise/)
- **Google Workspace CLI (`gws`)** — реальный инструмент Google, выпущен в марте 2026, open-source (Apache 2.0). Источник: [GitHub](https://github.com/googleworkspace/cli)
- **npm-пакет `@googleworkspace/cli`** — существует в npm registry. Установка: `npm install -g @googleworkspace/cli`. Источник: [npmjs.com](https://www.npmjs.com/package/@googleworkspace/cli)
- **Google Workspace CLI поддерживает MCP** — подтверждено, CLI включает MCP-совместимые agent skills. Источник: [GitHub](https://github.com/googleworkspace/cli)
- **Cowork работает с Google Docs, Google Sheets, Google Drive** — подтверждено через встроенные коннекторы и/или gws CLI. Источник: [Windows Forum](https://windowsforum.com/threads/claude-cowork-expands-with-google-drive-gmail-and-docusign-for-enterprise-ai.403254/)
- **Cowork создаёт документы напрямую (без copy-paste)** — подтверждено, ключевая функция продукта. Источник: [Anthropic](https://claude.com/product/cowork)
- **Cowork помнит контекст сессии** — подтверждено, агент сохраняет контекст в рамках одной сессии для итеративной работы. Источник: [Claude Cowork Starter Guide](https://claudiaplusai.substack.com/p/claude-cowork-starter-guide-30-examples)
- **Фреймворк «Что → Откуда → Куда → Формат»** — авторский методический приём курса, не является внешней технической сущностью. Фактчек не требуется
- **Google Sheets, Google Docs, Google Drive** — реальные сервисы Google Workspace. Подтверждено
- **Uzum Market, Korzinka** — реальные узбекские компании, корректно используются как примеры в контексте курса для аудитории в Узбекистане
