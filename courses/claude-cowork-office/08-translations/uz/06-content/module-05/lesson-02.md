# Avtomatlashtirish va natija / Dars 5.2: Murakkab skill'lar va avtomatlashtirish

## Metama'lumotlar

| Parametr | Qiymat |
|----------|--------|
| Modul | 5: Avtomatlashtirish va natija |
| Dars | 5.2 |
| Davomiyligi | 8 min |
| Turi | Nazariya |

## Video-skript

### Kirish (30 sek)

Assalomu alaykum! O'tgan darsda biz oddiy skill'lar — alohida vazifalar uchun shablonlar yaratdik. Lekin ko'plab ish jarayonlari ketma-ket bir necha bosqichdan iborat. Oy oxiriga tayyorgarlik — bu bitta hisobot emas, balki zanjir: ma'lumotlarni yig'ish, hisobot yaratish, taqdimot tayyorlash. Ushbu darsda murakkab skill'lar yaratishni va jadval bo'yicha avtomatik ishga tushirishni o'rganamiz.

### Asosiy qism

**Murakkab skill: bitta ko'rsatmada bosqichlar zanjiri**

Skill nafaqat bitta vazifani, balki butun zanjirni o'z ichiga olishi mumkin — 4-moduldagi pipeline kabi, lekin qayta foydalanish uchun saqlangan.

Misol: buxgalter uchun «Oy oxiri» skill'i:

**Nomi:** Oy oxiri

**Ko'rsatma:**
```
Oyning oxirgi ish kunida ishga tushiring.
Ketma-ket bajaring:
1. Google Sheets "Xarajatlar_[joriy oy]" ni oching.
   "Xulosa" varag'ini kategoriyalar bo'yicha yakunlar bilan yarating.
2. Xulosa asosida Google Docs da
   "Hisobotlar/Oylik" papkasida hisobot yarating: xarajatlar jadvali,
   o'tgan oy bilan taqqoslash, 3 ta xulosa.
3. Hisobot asosida Google Slides da
   6 slaydli taqdimot yarating "Taqdimotlar" papkasida:
   ko'rsatkichlar, dinamika, xulosalar, reja.
   Har bir slaydga speaker notes.
```

Ilgari yarim kun talab qiladigan uchta vazifa — endi bitta ibora: «Oy oxiri».

Bu alohida funksiya emas — bu bir necha bosqichli skill. Cowork ularni ketma-ket bajaradi, har bir bosqich natijasini keyingisiga uzatadi.

**Misol: «Haftalik rejalashtiruvchi» murakkab skill'i**

Bu skill uchrashuvga tayyorgarlik va natijalarni qayta ishlashni bitta ko'rsatmada birlashtiradi:

**Ko'rsatma:**
```
Tayyorgarlik (uchrashuvdan oldin):
1. Google Sheets "Vazifalar_jamoa" ni oching — haftalik
   statusni yig'ing.
2. Google Docs da "Rejalashtiruvlar" papkasida kun tartibini yarating:
   vazifalar statusi (jadval), muammoli vazifalar,
   muhokama uchun savollar.
3. Har bir bandga — tezislar (2-3 gap).
4. Oxirida bayonnoma shabloni: sana, ishtirokchilar,
   qarorlar, action items.
```

E'tibor bering: «oldin» tayyorgarlik va «keyin» qayta ishlash uchun — ikki alohida skill yaratish yaxshiroq, chunki ular orasida uchrashuv bo'ladi. Ikkinchi «Uchrashuv bayonnomasi» skill'i keyin ishga tushiriladi.

**CLAUDE.md ni skill'lar bilan birga qanday tashkil qilish**

Skill'lar alohida saqlanadi (Settings → Skills da), CLAUDE.md esa lavozimingiz kontekstini o'z ichiga oladi — bular turli narsalar va bir-birini to'ldiradi:

- **CLAUDE.md** — siz kim ekansiz, vazifalaringiz, hujjat formati, kompaniya qoidalari
- **Skills** — takrorlanuvchi vazifalar uchun aniq ko'rsatmalar

Cowork ikkalasidan foydalanadi: CLAUDE.md dan kontekstni (lavozim, format), skill'dan esa aniq bosqichlarni oladi. Shuning uchun CLAUDE.md da skill'larda mavjud ma'lumotni takrorlash shart emas.

CLAUDE.md uchun tavsiya etiladigan tuzilish:

```markdown
# Mening AI-assistentim

## Men haqimda
[Lavozim, bo'lim, kompaniya]

## Qoidalar
[Til, cheklovlar, xavfsizlik]

## Hujjat formati
[Hisobotlar, xatlar, jadvallarni qanday rasmiylashtirish]

## Ish papkalari
- Hisobotlar: Google Drive / Hisobotlar
- Rejalashtiruvlar: Google Drive / Rejalashtiruvlar
- Taqdimotlar: Google Drive / Taqdimotlar
```

Aniq topshiriqlar esa (juma hisoboti, rejalashtiruvga tayyorgarlik) — skill'larda.

**Scheduled tasks: jadval bo'yicha avtomatik ishga tushirish**

Cowork skill'larni jadval bo'yicha avtomatik ishga tushirish imkonini beradi. Siz sozlashingiz mumkin:

> «Har dushanba soat 9:00 da "Rejalashtiruvga tayyorgarlik" skill'ini ishga tushir»

Cowork vazifani bajaradi va natijani tekshirish uchun ko'rsatadi.

**Muhim cheklov:** scheduled tasks faqat kompyuter yoqilgan va Claude Desktop ochiq bo'lgandagina ishlaydi. Agar Mac uyqu rejimida yoki ilova yopiq bo'lsa — vazifa o'tkazib yuboriladi va keyingi uyg'onganda bajariladi. Bu lokal avtomatlashtirish, bulutli xizmat emas.

Amaliy maslahat: agar dushanba ertalabga vazifangiz bo'lsa — Claude Desktop kerakli vaqtdan oldin ishga tushirilganligiga ishonch hosil qiling. Yoki ilovani ochganingizda skill'ni qo'lda ishga tushiring.

| Vazifa | Jadval | Qachon sozlash |
|--------|--------|---------------|
| Rejalashtiruvga tayyorgarlik | Dush, 9:00 | Agar Mac ertalab yoqilgan bo'lsa |
| Juma hisoboti | Juma, 16:00 | Agar kun oxirigacha ishlasangiz |
| Oylik xulosa | Oxirgi kun, 14:00 | Agar Mac yoqilgan bo'lsa |

**Antipattern: haddan tashqari murakkab skill**

10 bosqichli skill yaratmang. Agar vazifa juda katta bo'lsa — 2-3 ta alohida skill'ga ajrating. Ikkita skill'ni ketma-ket ishga tushirish, bitta juda murakkab skill'ni sozlashdan osonroq.

### Xulosa (30 sek)

Murakkab skill — qayta foydalanish uchun saqlangan pipeline. Scheduled tasks esa skill'larni jadval bo'yicha avtomatik ishga tushirish imkonini beradi — lekin faqat Mac yoqilgan bo'lganda. Keyingi darsda Time Audit ga qaytamiz va aslida qancha vaqt tejashingizni o'lchaymiz.

## Matnli qo'llanma

### Murakkab skill va oddiy skill farqi

| | Oddiy skill | Murakkab skill |
|--|------------|----------------|
| Bosqichlar | 1 ta vazifa | Zanjirda 2-4 ta vazifa |
| Misol | «Juma hisoboti» | «Oy oxiri» (xulosa + hisobot + taqdimot) |
| Qachon foydalanish | Alohida takrorlanuvchi vazifa | Birga takrorlanadigan vazifalar zanjiri |

### Murakkab skill namunasi

**Nomi:** Oy oxiri

**Ko'rsatma:**
```
Oyning oxirgi ish kunida ishga tushiring.
1. Google Sheets "Xarajatlar_[oy]" → "Xulosa" varag'i
2. Xulosa → Google Docs da hisobot ("Hisobotlar/Oylik" papkasi)
3. Hisobot → Google Slides da 6 slaydli taqdimot
   ("Taqdimotlar" papkasi) + speaker notes
```

### CLAUDE.md + Skills: vazifalarni taqsimlash

| CLAUDE.md | Skills |
|-----------|--------|
| Siz kim ekansiz (lavozim, kompaniya) | Vazifalar uchun aniq ko'rsatmalar |
| Qoidalar va hujjat formati | Bajarish bosqichlari |
| Ish papkalari va vositalar | Ma'lumot manbalari va natijalar |

CLAUDE.md → kontekst. Skills → harakatlar.

### Scheduled tasks

**Imkoniyatlar:** skill'ni jadval bo'yicha avtomatik ishga tushirish (kunlik, haftalik, oylik).

**Cheklov:** faqat Mac yoqilgan va Claude Desktop ochiq bo'lganda ishlaydi. Agar kompyuter uyquda bo'lsa — vazifa o'tkazib yuboriladi.

**Tavsiya:** ertalabki vazifalar uchun Claude Desktop ishga tushirilganligiga ishonch hosil qiling. Yoki ilovani ochganingizda skill'ni qo'lda ishga tushiring.

## Asosiy xulosalar

1. **Murakkab skill** — qayta foydalanish uchun saqlangan, bir necha bosqichli pipeline. Oddiy skill kabi yaratiladi, lekin ko'rsatmada bir necha bosqich bilan
2. **CLAUDE.md va skill'lar bir-birini to'ldiradi:** CLAUDE.md kontekstni saqlaydi (lavozim, qoidalar, format), skill'lar — aniq ko'rsatmalarni. Ular orasida ma'lumotni takrorlamang
3. **Scheduled tasks** skill'larni jadval bo'yicha avtomatik ishga tushiradi, lekin faqat Mac yoqilgan va Claude Desktop ochiq bo'lganda — bu lokal avtomatlashtirish, bulutli xizmat emas
