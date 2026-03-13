# Knowledge Base — Reference файлы

Pipeline использует reference-файлы из корня проекта для обеспечения качества и соответствия стандартам OSNOVA.

## Текущие references

| Reference | Путь | Используется в |
|-----------|------|----------------|
| Ценности создания курсов | `foundation/course-design-values.md` | Stage 03 (PRD), Stage 04 |
| Tone of voice | `foundation/brand_tone_of_voice.md` | Stage 06 (Content) |

## Как добавить новый reference курс

1. Убедись что курс в формате OSNOVA (паспорт + модули + уроки с буллетами)
2. Добавь путь к файлу в таблицу выше
3. Обнови stage instructions, которые должны его использовать
4. В stage instructions добавь `Read` этого файла перед генерацией

## Зачем нужны references

- **Формат** — генерируемые курсы должны выглядеть как существующие
- **Стиль** — буллеты, примеры, уровень детализации
- **Качество** — benchmark для quality gates
