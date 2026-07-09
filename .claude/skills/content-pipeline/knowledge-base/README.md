# Knowledge Base — Reference файлы

Pipeline может опираться на reference-файлы из корня проекта для обеспечения качества и соответствия принятым в проекте стандартам. Эти файлы опциональны: если их нет, pipeline опирается на шаблоны из `templates/`.

## Какие references можно добавить

| Reference | Рекомендуемый путь | Используется в |
|-----------|------|----------------|
| Ценности / принципы создания курсов | `foundation/course-design-values.md` | Stage 02 (PRD), Stage 03 (Structure) |
| Tone of voice бренда | `foundation/brand_tone_of_voice.md` | Stage 04 (Content) |

## Как добавить новый reference курс

1. Убедись что курс в формате шаблона `templates/course-structure.md` (паспорт + модули + уроки с буллетами)
2. Добавь путь к файлу в таблицу выше
3. Обнови stage instructions, которые должны его использовать
4. В stage instructions добавь `Read` этого файла перед генерацией

## Зачем нужны references

- **Формат** — генерируемые курсы должны выглядеть как существующие
- **Стиль** — буллеты, примеры, уровень детализации
- **Качество** — benchmark для quality gates
