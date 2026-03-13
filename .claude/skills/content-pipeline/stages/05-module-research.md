# Stage 05: Module Research

## Задача

Провести глубокий research для каждого модуля курса параллельно через Task() субагенты. Результат — отдельный файл research на каждый модуль.

## Вход
- `04-structure.md` (approved)

## Выход
- `05-module-research/module-{nn}.md` — research для каждого модуля

## Инструкции

### 0. Roadmap

Покажи Roadmap (формат из SKILL.md) с `🔄 05 Module Research` как текущим этапом.

### 1. Парсинг модулей

Прочитай `courses/{slug}/04-structure.md`. Извлеки список модулей:
- Название модуля
- Цель модуля
- Уроки и их темы
- Инструменты/технологии

### 2. Генерация запросов

Для каждого модуля сгенерируй **3-5 research запросов** на английском, покрывающих:
- Лучшие практики преподавания темы модуля
- Актуальные примеры и кейсы для практических заданий
- Инструменты/фичи, которые нужно показать в уроках
- Типичные ошибки и misconceptions студентов

Покажи пользователю запросы для всех модулей.

Используй **AskUserQuestion**:
- question: "Запросы для модульного research готовы. Запускаем?"
- options: `["Запустить research", "Изменить запросы"]`

### 3. Параллельное исследование

Запусти **отдельный Task() субагент на каждый модуль**.

Каждый субагент:

```bash
python .claude/skills/perplexity-research/research.py \
  --topic "Module {nn}: {module_name} — {course_name}" \
  --questions "{запрос 1}" \
  --questions "{запрос 2}" \
  --questions "{запрос 3}" \
  --model sonar-pro \
  --output "courses/{slug}/05-module-research/module-{nn}.md" \
  --delay 1.5
```

Промпт для субагента:

```
Ты исследователь. Задача — провести research для модуля "{module_name}" курса "{course_name}".

Контекст модуля:
- Цель: {module_goal}
- Уроки: {lessons_list}

Запусти research.py с запросами: {queries}

Команда:
python {path_to_research_py} --topic "Module {nn}: {module_name}" --questions {queries_formatted} --model sonar-pro --output "courses/{slug}/05-module-research/module-{nn}.md" --delay 1.5

После получения результатов:
1. Прочитай сгенерированный файл
2. Добавь в начало файла контекст модуля (цель, уроки)
3. Добавь в конец краткое резюме (3-5 предложений): что найдено и как это применить в уроках
```

### 4. Сборка результатов

После завершения всех субагентов:
1. Проверь что каждый модуль получил свой файл в `05-module-research/`
2. Покажи пользователю краткий summary: какие модули исследованы, сколько источников

### 5. Обновление state

```json
{
  "stages": {
    "05-module-research": {
      "status": "completed",
      "completed_at": "{ISO datetime}",
      "metadata": {
        "modules_count": "{n}",
        "total_sources": "{n}"
      }
    }
  },
  "current_stage": "06-content"
}
```

### 6. Переход

Покажи Roadmap с обновлённым статусом `✅ 05 Module Research`.

Используй **AskUserQuestion**:
- question: "Module Research завершён. Перейти к генерации контента?"
- options: `["Продолжить к Content Generation", "Остановиться"]`

## Quality Checklist

- [ ] Каждый модуль имеет свой файл research
- [ ] Запросы покрывают практику, инструменты, ошибки студентов
- [ ] Каждый файл содержит контекст модуля и резюме
