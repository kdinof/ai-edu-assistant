# Fact-Check Report: Module 05

**Дата:** 2026-03-17
**Файлы:** lesson-01.md, lesson-02.md, lesson-03.md, lesson-04.md
**Сущностей проверено:** 14

## Результат: ISSUES FOUND

## Проблемы

### ⚠️ Неточности

| Сущность | Урок | Проблема | Актуальная информация | Источник |
|----------|------|----------|----------------------|----------|
| Skills хранятся в CLAUDE.md | 5.1, 5.2, 5.4 | Контент утверждает, что skills создаются как секции в CLAUDE.md и запускаются фразой «Запусти skill "Название"». В реальности Claude Cowork использует отдельные SKILL.md файлы в директориях `~/.claude/skills/your-skill-name/`. CLAUDE.md (Claude Code) не читается Cowork. Skills в Cowork также можно создавать через Settings > Capabilities > Skills > Add. | Skills хранятся в отдельных SKILL.md файлах с YAML frontmatter (name + description), а не как секции CLAUDE.md. Создание через `/skill-creator`, вручную в `~/.claude/skills/`, или через UI. | [Claude Help Center: Use Skills](https://support.claude.com/en/articles/12512180-use-skills-in-claude), [Claude Help Center: Create Custom Skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills), [Claude Code Docs: Skills](https://code.claude.com/docs/en/skills) |
| Scheduled tasks без ограничений | 5.2 | Контент представляет scheduled tasks как простую команду «Каждый понедельник в 9:00 запускай skill...» без упоминания ограничений. | Scheduled tasks работают ТОЛЬКО при включённом компьютере и открытом Claude Desktop. Если компьютер спит или приложение закрыто — задача пропускается (выполняется при следующем пробуждении). Это локальное выполнение, не облачная автоматизация. | [Claude Help Center: Schedule recurring tasks](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-cowork) |
| Структура CLAUDE.md: «Обо мне → Правила → Skills → Workflow» | 5.2, 5.4 | Рекомендуемая структура CLAUDE.md включает секции Skills и Workflow. Но CLAUDE.md — файл для Claude Code, а не для Cowork. Skills и workflow в Cowork организуются иначе. | Для Claude Code CLAUDE.md содержит project instructions (build commands, coding standards). Для Cowork skills хранятся отдельно в SKILL.md файлах. Концепция «workflow как секция в CLAUDE.md» не соответствует реальному механизму. | [Claude Code Docs: Memory](https://code.claude.com/docs/en/memory), [Claude Help Center: Get started with Cowork](https://support.claude.com/en/articles/13345190-get-started-with-cowork) |

### 🔍 Требует уточнения

| Сущность | Урок | Контекст использования | Комментарий |
|----------|------|----------------------|-------------|
| «Запусти skill "Название"» как способ вызова | 5.1, 5.4 | Утверждается, что skills запускаются фразой в чате. | В Cowork skills вызываются через slash-команду `/skill-name` или автоматически по описанию в YAML frontmatter. Фраза «Запусти skill» может сработать в чате, но это не документированный способ. Требует проверки автором. |
| Workflow как единая концепция Cowork | 5.2 | Контент описывает workflow как цепочку skills, объединённых в CLAUDE.md. | Cowork не имеет отдельной сущности «workflow». Цепочку задач можно описать в промпте или в skill, но это не выделенная функция продукта. |

## ✅ Проверено и подтверждено

- **Claude Cowork** — продукт существует, выпущен Anthropic в январе 2026 для Mac, февраль 2026 для Windows
- **Google Workspace CLI (`gws`)** — существует, npm-пакет `@googleworkspace/cli`, команды `gws auth setup`, `gws auth login` корректны
- **Google Workspace CLI + Claude интеграция** — подтверждено, CLI работает с Claude как инструмент через терминал
- **Claude Pro $20/мес** — ⚠️ CHECK PRICING — на март 2026 цена $20/мес (month-to-month) или $17/мес (годовая подписка), но цены меняются
- **Scheduled tasks в Cowork** — функция существует, доступна на всех платных планах (Pro, Max, Team, Enterprise)
- **Google Sheets, Google Docs, Google Slides, Google Drive** — все упоминания корректны как сервисы Google Workspace
- **MCP (Model Context Protocol)** — протокол существует, используется для интеграций
- **CLAUDE.md как файл инструкций** — файл существует и читается Claude Code автоматически
- **Google Calendar, Gmail** — корректно упомянуты как сервисы, с которыми работает `gws`
