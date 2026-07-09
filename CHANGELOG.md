# Changelog

## [2026-07-09]

### Изменено
- Пайплайн упрощён: убраны этапы Deep Research (Stage 02) и Module Research (было Stage 05) — единственным источником контента теперь являются референсы, загружаемые пользователем на Bootstrap. Удалён skill `perplexity-research` и команда `/course-research`
- Референсные материалы на Stage 01 (Bootstrap) стали обязательными — этап не завершается без хотя бы одного файла или ссылки
- Все стейджи перенумерованы: `02-prd → 02-prd`, `03-prd → 02-prd`, `04-structure → 03-structure`, `06-content → 04-content`, `07-tests → 05-tests`, `08-lesson-summaries → 06-lesson-summaries`, `09-translation → 07-translation`. В SKILL.md добавлен мэппинг для возобновления курсов со старой нумерацией
- Bootstrap-опросник (по фидбоку продюсера после сравнения с брифом HR-команды) сокращён с 9 блоков до 6: из «Целевой аудитории» убраны боли/JTBD/барьеры/мотивация (осталось: кто, уровень, что уже знает); удалены секции «Финальный артефакт», «Инструменты и технологии», «Конкурентный контекст», «Локальный контекст и языки»; формат курса зафиксирован по умолчанию как «текст + интерактивные HTML-материалы» и больше не спрашивается
- Stage 02 (PRD): инструменты теперь выводятся из референсов, а не из bootstrap; конкурентный анализ убран из PRD, шаблона и quality-gates
- Stage 07 (Translation) стал опциональным: целевые языки спрашиваются у пользователя при запуске этапа, а не берутся из bootstrap/PRD; перевод поддерживает произвольные языки (не только узбекский)
- Удалена привязка к бренду OSNOVA из CLAUDE.md, README, prd.md, roadmap.md и агентов (`git-changelog-push`, `lesson-summary-writer`, `uz-content-translator`) — пайплайн описан как платформо-независимый; пути agent-memory в агентах сделаны относительными
- Обновлены quality-gates.md, pipeline-stages.md и команды `course-structure`/`lesson-tests` под новую нумерацию стейджей

### Удалено
- Удалена папка `foundation/` (`brand_tone_of_voice.md`, `course-design-values.md`) и связанные references в стейджах
- Из README убраны требования Python 3.10+ и Perplexity API key, инструкции по настройке `.env`

## [2026-04-09]

### Добавлено
- Новый агент `git-changelog-push` — автоматизирует git commit, обновление CHANGELOG и push
- Поддержка референсных материалов в pipeline: папка `references/` и `links.md` на этапе Bootstrap, чтение файлов и ссылок во всех последующих этапах (02-06)
- Stage 07 (Tests): параллельная генерация тестов через отдельные Agent subagents на каждый модуль

### Изменено
- Stage 01 (Bootstrap): добавлен шаг 5 — сбор референсных материалов (файлы + ссылки), обновление `pipeline-state.json` с `has_references`
- Stage 02 (Research): анализ референсов пользователя перед Perplexity research, фокус запросов на пробелы
- Stage 03 (PRD): референсы пользователя как приоритетный источник для scope и learning outcomes
- Stage 05 (Module Research): учёт референсов при генерации запросов для субагентов
- Stage 06 (Content): референсы как основной источник контента урока, research — дополнение
- Stage 07 (Tests): переработан алгоритм — параллельные агенты вместо последовательной обработки
- SKILL.md: инициализация папки `references/` и поля `has_references` при создании курса
- `pipeline-stages.md`: обновлены входы этапов 02, 03, 05, 06; расширена схема `pipeline-state.json`
- Команда `lesson-tests`: добавлен инструмент `Agent` в список `allowed-tools`
- `.gitignore`: добавлены `courses/` и `docs/`

## 2026-03-23

**Add CHANGELOG, update README with upgrade instructions**

- Добавлен CHANGELOG.md для отслеживания изменений
- Добавлена инструкция по обновлению проекта в README (git pull, ZIP → git)

## 2026-03-19

**Improve Stage 01-02 pipeline based on producer feedback**

- Обновлён Stage 01 (Bootstrap): уточнён опросник
- Переработан Stage 02 (Research): расширены инструкции и шаблон research-report
- Обновлён шаблон bootstrap-questionnaire

## 2026-03-18

**Add ai-office-bundle course, claude-cowork-office tests/translations, pipeline updates**

- Добавлен новый курс `ai-office-bundle` (stages 01-04)
- Сгенерированы тесты для модулей 2-5 курса `claude-cowork-office`
- Переведены тесты модулей 2-5 на узбекский
- Обновлён pipeline-state

## 2026-03-17

**Add test generation skill, modules 4-5 content, tests for module 1, UZ translation**

- Добавлен skill генерации тестов (`lesson-tests`)
- Сгенерирован контент модулей 4-5 курса `claude-cowork-office`
- Созданы тесты для модуля 1
- Переведены уроки и тесты модуля 1 на узбекский
- Обновлён pipeline-state

## 2026-03-13

**Initial commit: AI Content Pipeline for online courses**

- Инициализация проекта: pipeline, skills, commands, templates
- Курс `claude-cowork-office`: stages 01-06 (bootstrap → content)
- Foundation: tone of voice, course design values
- PRD и roadmap
