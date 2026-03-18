# Jadvallar va ma'lumotlar / Dars 3.3: Formulali jadvallar yaratish

## Metama'lumotlar

| Parametr | Qiymati |
|----------|----------|
| Modul | 3: Jadvallar va ma'lumotlar |
| Dars | 3.3 |
| Davomiyligi | 7 min |
| Turi | Aralash |

## Video-skript

### Kirish (30 sek)

Assalomu alaykum! O'tgan darsda biz mavjud jadvallarni tahlil qildik. Endi teskari vazifa — noldan yangi jadval yaratish. Loyiha byudjeti, vazifalar trekeri, ish vaqti jadvali — ish uchun zarur bo'lgan har qanday tuzilmali jadval.

Cowork ga to'g'ri tuzilma va ishlaydigan formulalar bilan jadval yaratish topshirig'ini qanday berish kerakligini ko'rib chiqamiz.

### Asosiy qism

**Nega «jadval yasa» — yomon topshiriq**

Tasavvur qiling: hamkasbingizdan «byudjet uchun jadval yasa» deb so'raysiz. Qanday jadval yasaydi? Qanday ustunlar bilan? Qanday formulalar bilan? Qaysi davr uchun? Natijani qayta ishlashga to'g'ri kelishi aniq.

Cowork bilan ham xuddi shunday. «Loyiha byudjeti uchun jadval yarat» — juda mavhum. Mana nimalarni ko'rsatish kerak:

1. **Tuzilma:** qanday ustunlar va qatorlar
2. **Formulalar:** qanday hisob-kitoblar kerak
3. **Ma'lumotlar:** namunalar bilan to'ldirish yoki bo'sh qoldirish
4. **Format:** sarlavhalar, yakuniy qatorlar, varaqlar

**Namoyish: loyiha byudjeti**

Cowork ga topshiriq:

«Google Sheets da "Alfa loyihasi byudjeti Q2" jadvalini yarat. Tuzilma:
- Ustunlar: Turkum, Tavsif, Reja (so'm), Fakt (so'm), Og'ish (so'm), Og'ish (%)
- Turkumlar: Ish haqi, Ijara, Marketing, IT-infratuzilma, Xizmat safarlari, Vakolatxona xarajatlari, Boshqa
- Formulalar: Og'ish = Fakt - Reja. Og'ish % = (Fakt - Reja) / Reja. Reja, Fakt, Og'ish ustunlari bo'yicha yig'indili yakuniy qator
- Reja ustunini nollar bilan to'ldir, Fakt ni bo'sh qoldir»

Cowork nimalar yaratadi:
1. Ko'rsatilgan nom bilan yangi Google Sheet
2. Ustun sarlavhalari
3. 7 ta turkum qatori
4. «Og'ish» va «Og'ish %» ustunlarida formulalar
5. SUM-formulali yakuniy qator
6. «Reja» ustunida nollar, «Fakt» da bo'sh katakchalar

Endi siz «Reja» ustuniga haqiqiy raqamlarni kiritasiz, xarajatlar sarflanishi bilan — «Fakt» ustunini to'ldirasiz. Og'ishlar avtomatik hisoblanadi.

**Formulalar: sintaksis emas, so'zlar bilan tasvirlang**

Google Sheets formulalari sintaksisini bilishingiz shart emas. Vazifani oddiy tilda tasvirlang:

| Sizga nima kerak | Cowork ga qanday aytish kerak |
|------------------|-------------------------------|
| Ustun bo'yicha yig'indi | «D ustuni uchun yig'indi formulasi» |
| Bo'lim bo'yicha o'rtacha | «Bo'lim = "Marketing" bo'lgan qatorlar uchun sotuvlarning o'rtacha qiymati» |
| Umumiy summadan foiz | «Har bir qatorda — umumiy summadan foiz ulushi» |
| Shartli yig'indilash | «Turkumi "Marketing" va oyi "mart" bo'lgan xarajatlar yig'indisi» |
| Qiymat qidirish | «"Narxlar" varag'idagi jadvaldan tovar kodi bo'yicha narxni top» |

Cowork o'zi mos funksiyani — SUM, AVERAGE, SUMIF, SUMIFS, VLOOKUP, INDEX/MATCH — tanlaydi va formulani kerakli katakchaga qo'yadi.

**Odatiy jadval shablonlari**

Ko'pchilik ofislarda kerak bo'ladigan jadvallar uchun topshiriqlar. Asos sifatida foydalaning va o'zingizga moslang:

**Vazifalar trekeri:**
«"Bo'lim vazifalari trekeri" nomli Google Sheet yarat. Ustunlar: Vazifa, Mas'ul, Muddat, Holat (tanlov ro'yxati: Yangi/Jarayonda/Tekshiruvda/Tayyor), Muhimlik (Yuqori/O'rta/Past), Izoh. "Xulosa" nomli varaq qo'sh — har bir holat va har bir mas'ul bo'yicha vazifalar sonini hisoblash bilan».

**Tadbirlar rejasi:**
«"Q2 Tadbirlar rejasi" nomli Google Sheet yarat. Ustunlar: Tadbir, Sana, Joy, Byudjet (reja), Byudjet (fakt), Mas'ul, Holat. Byudjetlar yig'indisi bilan yakuniy qator. Alohida "Oylar bo'yicha" varag'i — har bir oy bo'yicha byudjetlar yig'indisi».

**Ish vaqti jadvali:**
«"Mart 2026 ish vaqti jadvali" nomli Google Sheet yarat. Qatorlar — xodimlar (10 qator, ismlarni bo'sh qoldir). Ustunlar — oy kunlari (1-31) va jami soatlar. Jami formulasi: barcha kunlar bo'yicha soatlar yig'indisi. Pastda — har bir kun bo'yicha jami».

**2-modul hujjatlari bilan bog'liqlik**

Jadvallar va hujjatlar birgalikda ishlaydi. Cowork Google Sheets dagi ma'lumotlarni Google Docs da hujjatlar yaratish uchun ishlatishi mumkin — va aksincha.

Misol: «"Alfa loyihasi byudjeti Q2" jadvalidagi ma'lumotlarni olib, Google Docs da rahbariyat uchun qisqacha ma'lumotnoma yarat: umumiy byudjet, eng katta 3 ta xarajat turkumi, rejadan og'ishlar».

Bu — payplayn, 4-modul mavzusi. Lekin hozirdanoq esda tuting: siz yaratgan har bir jadval hujjatlar va hisobotlar uchun ma'lumot manbai bo'lishi mumkin.

### Xulosa (30 sek)

Jadval yaratishda eng muhimi — batafsil tavsif: ustunlar tuzilmasi, kerakli formulalar, boshlang'ich ma'lumotlar. Formulalarni so'zlar bilan tasvirlang — Cowork o'zi to'g'ri funksiyani tanlaydi.

Keyingi darsda — amaliyot: siz o'zingizning haqiqiy ish ma'lumotlaringiz bilan jadval yaratib, tahlil qilasiz.

## Matnli qo'llanma

### Jadval yaratishda nimalarni ko'rsatish kerak

Mavhum «jadval yasa» oldindan aytib bo'lmaydigan natija beradi. To'rtta elementni ko'rsating:

1. **Tuzilma** — ustunlar, qatorlar, varaqlar
2. **Formulalar** — qanday hisob-kitoblar kerak (so'zlar bilan tasvirlang)
3. **Ma'lumotlar** — namunalar bilan to'ldirish yoki bo'sh qoldirish
4. **Format** — yakuniy qatorlar, sarlavhalar, tartiblash

### Formulalar oddiy tilda

Sintaksisni bilishingiz shart emas. Vazifani tasvirlang — Cowork funksiyani tanlaydi:

| Vazifa | Cowork ishlatiladigan funksiya |
|--------|-------------------------------|
| Ustun bo'yicha yig'indi | SUM |
| Shartli o'rtacha | AVERAGEIF |
| Shartli yig'indilash | SUMIF / SUMIFS |
| Umumiy summadan foiz | SUM ga bo'lish, katakchani mahkamlash ($) bilan |
| Kod bo'yicha qidirish | VLOOKUP / INDEX+MATCH |

### Odatiy ofis jadvallari shablonlari

**Loyiha byudjeti:** xarajat turkumlari, reja/fakt, summada va foizda og'ishlar, yakuniy qator.

**Vazifalar trekeri:** vazifa, mas'ul, muddat, holat (tanlov ro'yxati), muhimlik, holatlar bo'yicha xulosa.

**Ish vaqti jadvali:** xodimlar x oy kunlari, qatorlar va ustunlar bo'yicha jami.

**Tadbirlar rejasi:** tadbir, sana, byudjet reja/fakt, oylik xulosa.

### 2-modul bilan bog'liqlik

Google Sheets dagi har bir jadval — Google Docs dagi hujjatlar uchun potentsial ma'lumot manbai. Cowork Sheets dan ma'lumotlarni olib, Docs da hisobotlarni avtomatik shakllantirishga qodir.

## Asosiy xulosalar

1. **Tuzilmaning batafsil tavsifi** — yaxshi jadvalning kaliti. Ustunlar, qatorlar, formulalar va formatni ko'rsating. «Byudjet uchun jadval yasa» — yomon. Aniq ustunlar va formulalar bilan tavsif — yaxshi
2. **Formulalarni sintaksis bilan emas, so'zlar bilan tasvirlang.** «Turkumi "Marketing" bo'lgan xarajatlar yig'indisi» — Cowork o'zi SUMIF ni tanlab, to'g'ri formulani yozadi
3. **Jadvallar va hujjatlar birgalikda ishlaydi.** Google Sheets dagi ma'lumotlarni Google Docs da hisobotlar yaratish uchun ishlatish mumkin — bu 4-moduldagi payplaynlar asosi
