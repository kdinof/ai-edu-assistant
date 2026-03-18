# Jadvallar va ma'lumotlar / Dars 3.2: Mavjud jadvallarni tahlil qilish

## Metama'lumotlar

| Parametr | Qiymati |
|----------|----------|
| Modul | 3: Jadvallar va ma'lumotlar |
| Dars | 3.2 |
| Davomiyligi | 8 min |
| Turi | Aralash |

## Video-skript

### Kirish (30 sek)

Assalomu alaykum! Jadvallar bilan eng ko'p uchraydigan vazifa — yangi jadval yaratish emas, balki mavjudini tushunish. Sizda 500 qatorlik xarajatlar jadvali bor, va rahbar so'raydi: «Eng katta 5 ta xarajat moddalari qaysi? Oylar bo'yicha dinamika qanday o'zgargan?»

Bu darsda Google Sheets dagi mavjud ma'lumotlarni tahlil qilish bo'yicha Cowork ga topshiriq berishni o'rganamiz.

### Asosiy qism

**Asosiy tamoyil: aniq savollar, «tahlil qil» emas**

Eng keng tarqalgan xato — Cowork ga shunday yozish: «Bu jadvalni tahlil qil». Bu xuddi hamkasbingizga: «Shu raqamlarga qara va aqlli narsa ayt» — deyish bilan barobar. Natija noaniq bo'ladi.

To'g'ri yondashuv — ma'lumotlarga aniq savollar berish:

| Yomon | Yaxshi |
|-------|--------|
| «Xarajatlar jadvalini tahlil qil» | «Q1 uchun eng katta 5 ta xarajat turkumini top, har birining umumiy summadagi ulushini hisobla» |
| «Sotuvlar ma'lumotlarini ko'r» | «Yanvar va fevral sotuvlarini har bir menejer bo'yicha solishtir, kim o'sgan, kim tushgan — ko'rsat» |
| «Bu jadval haqida nima deysiz?» | «Anomaliyalarni top: summasi o'rtachadan 3 baravar ko'p farq qiladigan qatorlar» |

Savol qanchalik aniq bo'lsa — javob shunchalik foydali bo'ladi.

**Namoyish: xarajatlar jadvalini tahlil qilish**

Vazifani tasavvur qiling. Sizda "Xarajatlar 2026" nomli Google Sheet bor — 500 qator: sana, turkum, tavsif, summa, bo'linma.

Cowork ga topshiriq:

«Google Sheets dagi "Xarajatlar 2026" jadvalini och. Menga "Q1 Tahlili" nomli yangi varaqda tahlil kerak:
1. Yanvar-mart uchun eng katta 5 ta xarajat turkumi — summalar va umumiy xarajatlardan foiz
2. Oylar bo'yicha umumiy xarajatlar dinamikasi — yanvar, fevral, mart
3. Bo'linmalar bo'yicha xarajatlarni solishtirish
4. Summasi 5 000 000 so'mdan oshgan qatorlar — sanalar va tavsiflar ro'yxati»

Cowork nima qiladi:
1. Jadvalni MCP orqali ochadi, ma'lumotlarni o'qiydi
2. Xarajatlarni turkumlar bo'yicha guruhlaydi, summalar va foizlarni hisoblaydi
3. Dinamika uchun ma'lumotlarni oylar bo'yicha ajratadi
4. Solishtirish uchun bo'linmalar bo'yicha guruhlaydi
5. Yirik xarajatlarni filtrlab ajratadi
6. To'rtta ma'lumot bloki va formulalar bilan "Q1 Tahlili" nomli yangi varaq yaratadi

Natija — tuzilmali tahliliy varaq. Filtrlar va SUMIF bilan bir soatlik qo'lda ish o'rniga — 2 daqiqa.

**Ma'lumotlarga so'rovlarni qanday tuzish kerak**

2-moduldan olingan freymvorkni jadvallar uchun moslang:

**Nimani hisoblash kerak** — qanday ko'rsatkichlar, guruhlanishlar, taqqoslashlar kerak.
**Qaysi jadvaldan** — Google Sheets dagi fayl nomi, aniq varaq.
**Natijani qayerga joylashtirish** — shu jadvaldagi yangi varaq, yangi fayl yoki chatdagi javob.
**Qanday shaklda** — formulali jadval, matnli hisobot yoki ro'yxat.

Misol:

«"Q1 Sotuvlar" jadvalining "Ma'lumotlar" varag'idan har bir menejer bo'yicha o'rtacha bitim summasini hisobla. Natija — "O'rtacha bitim" nomli yangi varaqda, ustunlar: menejer, bitimlar soni, umumiy summa, o'rtacha summa. O'rtacha summa bo'yicha kattadan kichikka tartiblangan».

**Bir nechta varaqlar bilan ishlash**

Cowork bitta jadvalning bir nechta varag'i bilan ishlay oladi. Masalan:

«"Byudjet 2026" jadvalida "Reja" va "Fakt" varaqlarini solishtir. Fakt rejadan 15% dan ortiq oshgan turkumlarni top. Natija — "Og'ishlar" nomli yangi varaqda».

Cowork ikkala varaqni o'qiydi, qatorlarni turkumlar bo'yicha solishtiradi va og'ishlarni ko'rsatadi.

**Tahlilning odatiy vazifalari**

Cowork quyidagi vazifalarni ayniqsa yaxshi bajaradi:

- **Guruhlash va yig'indilash.** «Chorak davomida har bir bo'lim bo'yicha umumiy xarajatlarni hisobla»
- **Davrlarni solishtirish.** «Mart sotuvlarini fevral bilan solishtir — har bir mahsulot bo'yicha mutlaq va foizli o'sish»
- **Anomaliyalarni topish.** «Summasi o'rtachadan 3 standart og'ishdan ko'p farq qiladigan tranzaksiyalarni top»
- **Reytinglar.** «Xaridlar summasiga ko'ra eng yaxshi 10 ta mijoz va ularning umumiy sotuvlardagi ulushi»
- **Kross-jadval.** «Sotuvlarni menejerlar (qatorlar) va oylar (ustunlar) bo'yicha ajrat»

### Xulosa (30 sek)

Cowork orqali ma'lumotlarni tahlil qilishning asosiy qoidasi — mavhum «tahlil qil» o'rniga ma'lumotlarga aniq savollar berish. Nimani hisoblash kerak, qaysi jadvaldan, natijani qayerga joylashtirish va qanday formatda — ko'rsating.

Keyingi darsda teskari vazifa bilan shug'ullanamiz — noldan formulali yangi jadvallar yaratamiz.

## Matnli qo'llanma

### «Tahlil qil» o'rniga aniq savollar

Noaniq so'rovlar noaniq natijalar beradi. Cowork dan foydali tahlil olish uchun ma'lumotlarga aniq savollar bering.

| Noaniq so'rov | Aniq so'rov |
|---------------|-------------|
| «Xarajatlarni tahlil qil» | «Q1 uchun eng katta 5 ta xarajat turkumi — umumiy summadagi ulushi bilan» |
| «Sotuvlarni ko'r» | «Yanvar va fevral sotuvlarini har bir menejer bo'yicha solishtir» |
| «Qiziq narsa bormi?» | «Summasi o'rtachadan 3+ baravar farq qiladigan qatorlarni top» |

### Ma'lumotlarga so'rov freymvorki

1. **Nimani hisoblash kerak** — ko'rsatkichlar, guruhlanishlar, taqqoslashlar
2. **Qaysi jadvaldan** — fayl nomi va varaq
3. **Natijani qayerga joylashtirish** — yangi varaq, yangi fayl yoki chatdagi javob
4. **Qanday shaklda** — formulali jadval, matn, ro'yxat

### To'liq so'rov namunasi

> «Google Sheets dagi "Xarajatlar 2026" jadvalini och. "Q1 Tahlili" nomli yangi varaqda:
> 1. Q1 uchun eng katta 5 ta xarajat turkumi — summalar va umumiy xarajatlardan foiz
> 2. Oylar bo'yicha xarajatlar dinamikasi (yanvar-mart)
> 3. Bo'linmalar bo'yicha solishtirish
> 4. 5 000 000 so'mdan yuqori xarajatlar ro'yxati»

### Tahlilning odatiy vazifalari

- **Guruhlash:** har bir bo'lim bo'yicha xarajatlar yig'indisi
- **Davrlarni solishtirish:** oydan oyga sotuvlar o'sishi
- **Anomaliyalar:** 3 standart og'ishdan tashqariga chiqqan tranzaksiyalar
- **Reytinglar:** xaridlar summasiga ko'ra eng yaxshi 10 ta mijoz
- **Kross-jadvallar:** menejerlar (qatorlar) va oylar (ustunlar) bo'yicha sotuvlar

## Asosiy xulosalar

1. **Ma'lumotlarga aniq savollar** foydali natijalar beradi. «Jadvalni tahlil qil» — yo'q. «Eng katta 5 ta xarajat turkumini umumiy summadagi ulushi bilan top» — ha
2. **So'rov freymvorki:** Nimani hisoblash → Qaysi jadvaldan → Natijani qayerga → Qanday shaklda. Har bir band qanchalik aniq bo'lsa, natija shunchalik yaxshi bo'ladi
3. **Cowork** guruhlash, davrlarni solishtirish, anomaliyalarni topish va reytinglar bilan a'lo ishlaydi — qo'lda filtrlar va formulalar bilan soatlab vaqt talab qiladigan vazifalar bilan
