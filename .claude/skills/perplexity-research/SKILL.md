---
name: perplexity-research
description: "Deep web research using Perplexity API. Use when user needs: (1) comprehensive research on a topic with sources, (2) market analysis or competitive research, (3) fact-checking with citations, (4) collecting and synthesizing information from multiple sources into a structured document."
---

# Perplexity Research Skill

Глубокие исследования в интернете с использованием Perplexity API. Real-time поиск с цитированием источников.

## When to Use This Skill

**Используй когда:**
- Поиск актуальной информации (2024-2025)
- Исследование рынка и конкурентов
- Fact-checking с источниками
- Литературный обзор и тренды
- Информация за пределами knowledge cutoff модели
- Сбор данных для принятия решений

**НЕ используй для:**
- Простых вычислений или логических задач
- Задач, требующих выполнения кода
- Вопросов, на которые Claude может ответить без поиска
- Конфиденциальной информации

## Quick Start

### 1. Проверка настройки

```bash
python .claude/skills/perplexity-research/search.py --check-setup
```

### 2. Простой поиск

```bash
python .claude/skills/perplexity-research/search.py "EdTech рынок Узбекистан 2025"
```

### 3. Комплексное исследование

```bash
python .claude/skills/perplexity-research/research.py \
  --topic "Анализ EdTech рынка" \
  --questions "Размер рынка?" \
  --questions "Ключевые игроки?" \
  --output research/report.md
```

## Available Models

| Модель | Описание | Когда использовать | Цена |
|--------|----------|-------------------|------|
| `sonar` | Базовая | Простые факты, быстрые запросы | ~$0.001 |
| `sonar-pro` | Продвинутая (default) | Глубокий анализ, сложные темы | ~$0.003 |
| `sonar-reasoning` | С reasoning | Аналитические задачи, step-by-step | ~$0.005 |

**Выбор модели:**
- По умолчанию → `sonar-pro`
- Сложный многошаговый анализ → `sonar-reasoning`
- Простые факты, экономия → `sonar`

## Crafting Effective Queries

### Хорошие запросы

```
✓ "Какие EdTech стартапы в Узбекистане получили инвестиции в 2024 году?
   Укажи суммы раундов и инвесторов."

✓ "Сравни модели подписок Coursera, Udemy и Skillshare:
   цены, features, retention rates по данным 2024."

✓ "Какие best practices онбординга в SaaS продуктах
   показали рост activation rate в исследованиях 2023-2025?"
```

### Плохие запросы

```
✗ "EdTech" (слишком размыто)
✗ "Расскажи про онбординг" (нет специфики)
✗ "Курсы в интернете" (нет контекста)
```

### Структура эффективного запроса

1. **Тема**: Главный предмет
2. **Скоуп**: Конкретный аспект
3. **Контекст**: Временные рамки, домен, ограничения
4. **Формат**: Желаемый тип ответа

**Пример:**
```
"Какие изменения в поведении пользователей EdTech продуктов
произошли после COVID-19 в СНГ регионе?
Фокус на retention и engagement метриках,
данные исследований 2023-2024."
```

## Usage Examples

### Исследование рынка

```bash
python .claude/skills/perplexity-research/search.py \
  "EdTech market size Central Asia 2024-2025, growth projections, key players" \
  --model sonar-pro \
  --output research/market-analysis.md
```

### Конкурентный анализ

```bash
python .claude/skills/perplexity-research/research.py \
  --topic "Competitor Analysis: Online Education Uzbekistan" \
  --questions "Who are the main EdTech competitors in Uzbekistan?" \
  --questions "What pricing models do they use?" \
  --questions "What are their unique value propositions?" \
  --output research/competitors.md
```

### Best Practices Research

```bash
python .claude/skills/perplexity-research/search.py \
  "SaaS onboarding best practices 2025, activation rate optimization,
   user research findings" \
  --model sonar-reasoning
```

### Trend Analysis

```bash
python .claude/skills/perplexity-research/research.py \
  --topic "EdTech Trends 2025" \
  --questions "What are the key EdTech trends in 2025?" \
  --questions "How is AI changing online education?" \
  --questions "What engagement strategies show best results?" \
  --model sonar-pro \
  --output research/trends-2025.md
```

## Batch Processing

### Файл с вопросами

```bash
# questions.txt
What is the EdTech market size in Uzbekistan?
Who are the main competitors?
What pricing strategies work best?
What are the user acquisition channels?
```

```bash
python .claude/skills/perplexity-research/research.py \
  --topic "EdTech Market Research" \
  --questions-file questions.txt \
  --output research/full-report.md \
  --delay 2.0
```

### Bash batch script

```bash
#!/bin/bash
queries=(
  "EdTech market Uzbekistan 2025"
  "Online education trends CIS region"
  "Student engagement best practices"
)

for query in "${queries[@]}"; do
  python .claude/skills/perplexity-research/search.py "$query" \
    --output "research/$(echo $query | tr ' ' '_').md"
  sleep 2
done
```

## Programmatic Access

```python
from search import search_perplexity

result = search_perplexity(
    query="EdTech trends 2025",
    model="sonar-pro",
)

if "error" not in result:
    print(result["content"])
    print(f"Sources: {len(result['citations'])}")
```

## Setup

### API Key

Файл `.env` в корне проекта (уже настроено):

```
PERPLEXITY_API_KEY=pplx-your-key-here
```

Или переменная окружения:

```bash
export PERPLEXITY_API_KEY="pplx-your-key-here"
```

### Проверка

```bash
python .claude/skills/perplexity-research/search.py --check-setup
```

## Cost Management

**Оптимизация расходов:**
1. Используй `sonar` для простых запросов
2. `sonar-pro` — для большинства задач
3. `sonar-reasoning` — только когда нужен step-by-step анализ
4. Ограничивай `--max-tokens` для коротких ответов
5. Добавляй `--delay` между batch запросами

**Примерные затраты:**
- 10 простых запросов (sonar): ~$0.01
- 10 глубоких запросов (sonar-pro): ~$0.03
- Полное исследование (5-7 вопросов): ~$0.02-0.05

## Troubleshooting

### API Key Not Found

```
Error: PERPLEXITY_API_KEY not found
```

**Решение:** Проверь `.env` файл или установи переменную окружения.

### Rate Limiting

```
Error: Rate limit exceeded
```

**Решение:** Добавь задержку между запросами (`--delay 2.0`).

### Request Timeout

```
Error: Request timed out
```

**Решение:** Упрости запрос или попробуй позже.

### Invalid API Key

```
Error: Invalid API key
```

**Решение:** Проверь ключ на https://www.perplexity.ai/settings/api

## Integration with Other Skills

### С `growth-pm-edtech`

1. Используй Perplexity для market research
2. Передай данные в growth-pm для анализа
3. Получи actionable рекомендации

### С `product-researcher`

1. Perplexity для desk research перед интервью
2. Найди industry benchmarks
3. Подготовь контекст для JTBD вопросов

### С `xlsx`

1. Собери данные через Perplexity
2. Структурируй в таблицу через xlsx
3. Добавь визуализацию

## CLI Reference

### search.py

```
python search.py [QUERY] [OPTIONS]

Arguments:
  QUERY                 Search query

Options:
  --query, -q          Search query (alternative)
  --model, -m          Model: sonar, sonar-pro, sonar-reasoning
  --output, -o         Output file path
  --recency, -r        Filter: day, week, month, year
  --json               Output raw JSON
  --no-metadata        Skip metadata header
  --check-setup        Verify API configuration
```

### research.py

```
python research.py [OPTIONS]

Options:
  --topic, -t          Research topic (required)
  --questions, -q      Research question (multiple)
  --questions-file, -f File with questions
  --output, -o         Output report path
  --model, -m          Model to use
  --delay, -d          Delay between requests (seconds)
  --json               Output raw JSON
```

## Best Practices Summary

1. **Конкретные запросы** — включай домен, временные рамки, контекст
2. **Правильная модель** — match complexity to model
3. **Итеративный подход** — уточняй запросы на основе результатов
4. **Верифицируй** — проверяй критичные факты в первичных источниках
5. **Структурируй** — используй research.py для комплексных исследований
6. **Сохраняй** — всегда используй `--output` для важных исследований
