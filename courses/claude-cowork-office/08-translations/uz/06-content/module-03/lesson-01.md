# Jadvallar va ma'lumotlar / Dars 3.1: Claude + Google Sheets: nimalar mumkin

## Metama'lumotlar

| Parametr | Qiymati |
|----------|----------|
| Modul | 3: Jadvallar va ma'lumotlar |
| Dars | 3.1 |
| Davomiyligi | 5 min |
| Turi | Nazariya |

## Video-skript

### Kirish (30 sek)

Assalomu alaykum! O'tgan modulda biz Cowork va Google Docs orqali hujjatlar yaratishni o'rgandik. Lekin hujjatlar — bu ofis ishining faqat yarmi. Ikkinchi yarmi — jadvallar: hisobotlar, byudjetlar, tahlillar, trekerlar.

Bu darsda Claude Cowork MCP orqali Google Sheets bilan nimalar qila olishini — va uning imkoniyatlari chegarasi qayerda ekanini ko'rib chiqamiz.

### Asosiy qism

**Cowork Google Sheets bilan MCP orqali nimalar qiladi**

Siz 1-modulda Google Workspace MCP ni ulagan edingiz — shunda Cowork nafaqat Docs, balki Sheets ga ham kirish huquqini oldi. Mana u nimalar qila oladi:

**Ma'lumotlarni o'qish.** Cowork Google Drive dagi istalgan jadvalni ochishi, varaqlar tarkibini o'qishi, ma'lumotlar tuzilishini — sarlavhalar, ustun turlari, qatorlar sonini — tushunishi mumkin.

**Tahlil qilish.** Siz so'raysiz: «Chorak davomidagi eng katta 5 ta xarajat turkumi qaysi?» — Cowork ma'lumotlarni o'qiydi, yig'indilarni hisoblaydi, tartiblaydi va javob beradi. Faqat matn emas — u natijani o'sha jadvalda yangi varaqda yaratishi mumkin.

**Noldan jadval yaratish.** «Q2 uchun loyiha byudjetini Google Sheets da yarat» — va Cowork ustunlar, qatorlar va formatlash bilan yangi jadval yaratadi.

**Formulalar yozish.** SUMIF yoki VLOOKUP sintaksisini eslab o'tirish o'rniga, vazifani so'z bilan tasvirlaysiz: «Har bir menejer bo'yicha sotuvlar yig'indisini hisobla». Cowork formulani o'zi yozadi va kerakli katakchaga qo'yadi.

**Ma'lumot qo'shish.** Cowork mavjud jadvalga qatorlar qo'shishi mumkin — masalan, yangi yozuvlar kiritish yoki ma'lumotlarni yangilash.

**Namoyish: xom ma'lumotlardan xulosalargacha bir daqiqada**

Faraz qilaylik, sizda bir oylik sotuvlar jadvali bor — 300 qator: sanalar, menejerlar, summalar va tovar turkumlari.

Cowork ga topshiriq: «Google Sheets dagi "Mart savdolari" jadvalini och. Sotuvlar summasiga ko'ra eng yaxshi 3 menejerni top, haftalik dinamikani hisobla, "Tahlil" nomli yangi varaq yarat va natijalarni joylashtir».

Nima sodir bo'ladi:
1. Cowork jadvalni MCP orqali o'qiydi
2. Ma'lumotlarni menejerlar bo'yicha guruhlaydi, yig'indilarni hisoblaydi
3. Sotuvlarni haftalarga bo'ladi
4. Ikkita jadval bilan yangi varaq yaratadi: menejerlar reytingi va haftalik dinamika
5. Yakuniy natijalar uchun formulalar qo'shadi

Natija — jadvalingizdagi tayyor tahliliy varaq. Nusxalashsiz, formulalarni qo'lda yaratishsiz.

**Cheklovlar: Cowork nimalarni yaxshi bajara olmaydi**

Chegaralarni bilish muhim:

- **Grafiklar va diagrammalar.** Google Sheets MCP hozircha grafiklar yaratishni qo'llab-quvvatlamaydi. Cowork ma'lumotlarni tayyorlaydi, lekin vizualizatsiyani Sheets da qo'lda qo'shishingiz yoki Cowork dan code execution orqali grafikli Excel fayl yaratishini so'rashingiz kerak.
- **Murakkab makroslar va skriptlar.** Apps Script — MCP hududiga kirmaydi. Agar skriptlar darajasida avtomatlashtirish kerak bo'lsa, bu alohida vazifa.
- **Juda katta jadvallar (10 000+ qator).** MCP ma'lumotlarni matn sifatida uzatadi va katta hajmlarda sekin ishlashi mumkin. Bunday vazifalar uchun ma'lumotlarni oldindan filtrlash yaxshiroq.
- **Katakchalar formatlash.** Cowork ma'lumotlar va formulalar yozishi mumkin, lekin nozik formatlash (ranglar, to'ldirish, katakchalarni birlashtirish) hozircha cheklangan.

**Qoida:** Cowork ni tuzilma, ma'lumotlar va formulalar uchun ishlating. Yakuniy vizual bezash — Google Sheets ning o'zida.

### Xulosa (30 sek)

Xulosa qilib aytganda, Cowork MCP orqali Google Sheets da ma'lumotlarni o'qiy oladi, tahlil qiladi, jadvallar yaratadi va formulalar yozadi. Cheklovlar — grafiklar, makroslar va juda katta ma'lumotlar massivlari.

Keyingi darsda amaliyotga o'tamiz: mavjud jadvallardagi haqiqiy ma'lumotlarni tahlil qilish bo'yicha topshiriqlar berishni o'rganamiz.

## Matnli qo'llanma

### Cowork Google Sheets bilan nimalar qila oladi

Claude Cowork MCP orqali Google Sheets ga ulangan. Bu unga jadvallar bilan bevosita ishlash imkonini beradi — nusxalash va ma'lumotlarni qo'lda ko'chirishsiz.

| Imkoniyat | Misol |
|-----------|-------|
| Ma'lumotlarni o'qish | Jadvalni ochish, istalgan varaq tarkibini o'qish |
| Tahlil | Yig'indilarni hisoblash, tendentsiyalarni topish, ma'lumotlarni guruhlash |
| Jadval yaratish | Kerakli tuzilma bilan yangi Sheet yaratish |
| Formulalar | Oddiy tilda tasvirlangan holda SUM, SUMIF, VLOOKUP va boshqa formulalarni yozish |
| Ma'lumot qo'shish | Qatorlar qo'shish, qiymatlarni yangilash |

### Nimalar yaxshi ishlamaydi

| Cheklov | Nima qilish kerak |
|---------|-------------------|
| Grafiklar va diagrammalar | Ma'lumotlarni Cowork tayyorlaydi, vizualizatsiyani Sheets da qo'lda qo'shing |
| Apps Script va makroslar | MCP dan tashqari alohida vazifa |
| 10 000+ qatorli jadvallar | Ma'lumotlarni oldindan filtrlang |
| Nozik formatlash | Cowork ma'lumotlarni yozadi, yakuniy bezash — qo'lda |

### Amalda bu qanday ko'rinadi

Topshiriq: «"Mart savdolari" jadvalini och. Sotuvlar summasiga ko'ra eng yaxshi 3 menejerni top, haftalik dinamikani hisobla, "Tahlil" varag'ini natijalar bilan yarat».

Natija: Google Sheets da menejerlar reytingi, haftalik dinamika va yakuniy natijalar uchun formulalar bilan yangi varaq. Hammasi MCP orqali, qo'lda ishsiz yaratilgan.

## Asosiy xulosalar

1. **Cowork MCP orqali** Google Sheets da ma'lumotlarni o'qiydi, tahlil qiladi, jadvallar yaratadi va formulalar yozadi — nusxalash va qo'lda ko'chirishsiz
2. **Cheklovlar** — grafiklar, Apps Script, juda katta jadvallar (10 000+ qator) va nozik katakcha formatlash. Bu vazifalar uchun Google Sheets ni bevosita ishlating
3. **Vazifalar taqsimoti qoidasi:** Cowork tuzilma, ma'lumotlar va formulalar uchun javobgar. Yakuniy vizual bezash — Google Sheets ning o'zida
