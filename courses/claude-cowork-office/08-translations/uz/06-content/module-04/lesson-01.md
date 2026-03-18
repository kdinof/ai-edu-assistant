# Taqdimotlar va payplaynlar / Dars 4.1: Claude orqali taqdimotlar

## Metama'lumotlar

| Parametr | Qiymati |
|----------|----------|
| Modul | 4: Taqdimotlar va payplaynlar |
| Dars | 4.1 |
| Davomiyligi | 7 daq |
| Turi | Nazariya |

## Video-skript

### Kirish (30 sek)

Assalomu alaykum! Oldingi modullarda siz Google Docs'da hujjatlar yaratishni va Google Sheets bilan ishlashni o'rgandingiz. Ammo hali bir format bor — usiz birorta ham ish haftasi o'tmaydi — bu taqdimotlar. Ushbu darsda Cowork taqdimotlarni qanday yaratishini va uning nimani yaxshi, nimani yaxshi bajara olmasligini ko'rib chiqamiz.

### Asosiy qism

**Taqdimotlarga ikki yondashuv**

Cowork'da taqdimot yaratishning ikki usuli bor:

**1-yondashuv: Google Slides — Google Workspace CLI orqali.** Cowork taqdimotni bevosita Google Slides'da yaratadi — slaydlar, matn, jadvallar qo'shadi. Natija — Google Drive'dagi tayyor fayl, uni darhol ochib ko'rsatish mumkin.

Afzalliklari: fayl darhol Google Slides'da, birgalikda tahrirlash mumkin, hech narsa yuklab olish shart emas.
Cheklovlari: oddiy bezak — murakkab dizayn, animatsiyalar, nostandart maketlar yo'q.

**2-yondashuv: PPTX — code execution orqali.** Cowork PowerPoint-faylni dasturiy ravishda yaratadi — Python kutubxonasi `python-pptx` orqali. Bu ko'proq nazorat beradi: elementlarni aniq joylashtirish, ranglar, shriftlar, grafiklar.

Afzalliklari: yanada moslashuvchan dizayn, grafiklar qo'shish va bezakni aniq sozlash imkoniyati.
Cheklovlari: faylni yuklab olish va PowerPoint yoki Google Slides'da ochish kerak. Yuklanmaguncha birgalikda tahrirlash imkoni yo'q.

**Qaysi yondashuvni tanlash kerak?**

Oddiy qoida:

- **Ish taqdimotlari** (loyiha holati, rahbar uchun hisobot, uchrashuv kun tartibi) → Google Slides — gws orqali. Tez, qulay, har doim qo'l ostida.
- **Tashqi auditoriya uchun taqdimotlar** (mijoz, hamkor, konferensiya) → PPTX, agar dizayn muhim bo'lsa. Yoki Google Slides + muharrirda qo'lda ishlov berish.

Ko'pchilik ish vaziyatlarida — Google Slides — gws orqali.

**Taqdimot yaratish uchun vazifani qanday qo'yish kerak**

2-moduldagi freymvorkni ishlating — Nima → Qayerdan → Qayerga → Format:

Topshiriq namunasi:
> «Google Slides'da 8 slaydlik taqdimot yarat, choraklik hisobot natijalari bo'yicha. Ma'lumotlarni Google Sheets "Savdo_Q1_2026" va matnni Google Docs "Hisobot Q1"dan ol. Tuzilma: titul slayd, asosiy ko'rsatkichlar, oylar bo'yicha dinamika, top-5 mahsulot, muammolar, Q2 reja, xulosalar. Google Drive'dagi "Taqdimotlar" papkasiga saqlа.»

E'tibor bering: siz slaydlar tuzilmasini, ma'lumot manbalarini va papkani ko'rsatdingiz — Cowork taxmin qilmaydi.

**Namoyish: hisobotdan taqdimot**

Faraz qilaylik, Google Docs'da tayyor choraklik hisobotingiz bor, Google Sheets'da esa raqamlar jadvali. Siz Cowork'ga rahbariyat uchun taqdimot yaratish vazifasini berasiz.

Nima sodir bo'ladi:
1. Cowork hisobotni Google Docs'dan o'qiydi
2. Google Sheets'dan ma'lumotlarni o'qiydi
3. Google Slides'da taqdimot yaratadi: titul slayd, ko'rsatkichlar jadvali, xulosalar, tavsiyalar
4. Har bir slaydga speaker notes qo'shadi — nutq uchun tezislar
5. Ko'rsatilgan papkaga saqlaydi

Natija: ikki manbadan tayyor taqdimot 2-3 daqiqada.

**Claude nimani yaxshi bajaradi va nimani — yo'q**

| Yaxshi | Unchalik emas |
|--------|----------|
| Slaydlarning tuzilmasi va mantiqi | Murakkab vizual dizayn |
| Asosiy tezislar (matnni ortiqcha yuklamas) | Animatsiyalar va o'tishlar |
| Ma'lumotli jadvallar | Nostandart maketlar |
| Speaker notes | Infografika |
| Sheets va Docs'dan ma'lumotlarni birlashtirish | Brendlangan shablonlar |

Muhim: Claude taqdimotning **kontentini** yaratadi, dizaynini emas. Agar chiroyli bezak kerak bo'lsa — Google Slides'da korporativ shablonni ishlating va Cowork'dan uni mazmun bilan to'ldirishni so'rang.

### Xulosa (30 sek)

Xulosa qilib aytganda, ish taqdimotlari uchun Google Slides'ni gws orqali ishlating — tez va qulay. Claude tuzilma, tezislar va speaker notes bilan ajoyib ishlaydi, ammo dizaynni qo'lda yakunlash yoki tayyor shablondan foydalanish yaxshiroq. Keyingi darsda hammasini birga yig'amiz: Sheets'dan ma'lumotlar → Docs'da hisobot → taqdimot — bitta payplayn ichida.

## Matnli qo'llanma

### Taqdimotlarga ikki yondashuv

| Parametr | Google Slides (gws) | PPTX (code execution) |
|----------|---------------------|----------------------|
| Format | Google Drive'da Google Slides | .pptx fayl |
| Dizayn | Oddiy | Yanada moslashuvchan |
| Kirish | Darhol brauzerda | Yuklab olish kerak |
| Birgalikda ishlash | Ha | Drive'ga yuklangandan keyin |
| Qachon yaxshiroq | Ish taqdimotlari | Mijozlar uchun taqdimotlar |

### Qachon qaysi yondashuv

- **Google Slides (gws):** holat-hisobot, uchrashuv kun tartibi, rahbariyat uchun choraklik hisobot — tezda yaratib, darhol ko'rsatish kerak bo'lgan har qanday taqdimot
- **PPTX:** mijoz, konferensiya yoki hamkor uchun taqdimot — vizual dizayn muhim bo'lganda

### Topshiriq namunasi

```
Google Slides'da 8 slaydlik taqdimot yarat,
choraklik hisobot natijalari bo'yicha.

Manbalar:
- Google Sheets "Savdo_Q1_2026" — raqamlar va ko'rsatkichlar
- Google Docs "Hisobot Q1" — xulosalar va tavsiyalar

Slaydlar tuzilmasi:
1. Titul: nomi, davr, muallif
2. Asosiy ko'rsatkichlar: tushum, bitimlar, o'rtacha chek
3. Oylar bo'yicha dinamika: yanvar-mart jadvali
4. Tushum bo'yicha top-5 mahsulot
5. Muammolar va xavflar
6. Q2 reja
7. Xulosalar va tavsiyalar
8. Savollar

Har bir slaydga — speaker notes (2-3 gap).
Google Drive'dagi "Taqdimotlar" papkasiga saqlа.
```

### Claude'ning taqdimotlardagi kuchli va zaif tomonlari

**Kuchli:**
- Slaydlarning mantiqiy tuzilmasi
- Qisqa tezislar (matnni ortiqcha yuklamas)
- Google Sheets'dan ma'lumotli jadvallar
- Nutq uchun speaker notes
- Bir nechta manbadan ma'lumotlarni birlashtirish

**Zaif:**
- Murakkab dizayn yo'q (gradientlar, nostandart maketlar)
- Slaydlar orasida animatsiyalar va o'tishlar yo'q
- Brendlangan shablonlar bilan avtomatik ishlamaydi
- Infografika va murakkab grafiklar — cheklangan

**Tavsiya:** korporativ shablonni ishlating → Cowork'dan mazmun bilan to'ldirishni so'rang.

## Asosiy xulosalar

1. **Ikki yondashuv:** Google Slides — gws orqali (tez, ish vazifalari uchun) va PPTX — code execution orqali (dizayn ustidan ko'proq nazorat, tashqi taqdimotlar uchun). Ko'pchilik hollarda Google Slides — optimal tanlov
2. **Topshiriq = Nima → Qayerdan → Qayerga → Format.** Slaydlar tuzilmasini, ma'lumot manbalarini (Sheets, Docs) va saqlash papkasini ko'rsating — Claude bir nechta manbadan taqdimotni daqiqalar ichida yaratadi
3. **Claude kontent yaratadi, dizayn emas.** Tuzilma, tezislar, jadvallar, speaker notes — ajoyib. Murakkab vizual dizayn — qo'lda yakunlang yoki korporativ shablondan foydalaning
