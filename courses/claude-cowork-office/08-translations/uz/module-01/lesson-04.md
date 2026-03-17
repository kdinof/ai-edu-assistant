# AI-ofisni sozlash / Dars 1.4: Amaliyot: AI-ofisimizni sozlaymiz

## Metama'lumotlar

| Parametr | Qiymat |
|----------|--------|
| Modul | 1: AI-ofisni sozlash |
| Dars | 1.4 |
| Davomiyligi | 10 daq |
| Turi | Amaliyot |

## Video-skript

### Kirish (30 sek)

Oldingi darslarda nazariyani ko'rib chiqdik: agent chat-botdan nimasi bilan farq qiladi, Cowork'ni qanday o'rnatish va Google Workspace CLI'ni ulash, CLAUDE.md nima uchun kerak. Endi bularning hammasini qilamiz. Ushbu darsda siz o'z AI-ofisingizni sozlaysiz va "oldin" Time Audit'ni to'ldirasiz — joriy vazifalaringizga qancha vaqt ketayotganini qayd qilasiz.

### Asosiy qism

**1-topshiriq: O'rnatishni tekshiring (2 daq)**

Claude Desktop'ni oching va cheklistdan o'ting:

- [ ] Claude Desktop o'rnatilgan va ishga tushirilgan
- [ ] Cowork varag'i mavjud
- [ ] Google Workspace CLI ulangan (Claude Google Drive'dagi fayllaringizni ko'ra olyapti)

Agar Google Workspace CLI hali sozlanmagan bo'lsa — 1.2-darsga qayting va qadamlarni bajaring. Usiz kursning qolgan modullari ishlamaydi.

Ulanishni tekshiring — Cowork'da yozing:
> "Google Drive'dagi fayllarim ro'yxatini ko'rsat"

Claude fayllaringiz ro'yxatini qaytarishi kerak.

**2-topshiriq: CLAUDE.md yarating (5 daq)**

Lavozimingiz uchun CLAUDE.md yarating. 1.3-darsdagi shablondan foydalaning:

1. Siz kim ekansiz: lavozim, bo'lim, kompaniya
2. Har hafta bajaradigan 4-5 ta odatiy vazifani sanab o'ting
3. Kompaniyangizda qabul qilingan hujjat formatini ko'rsating
4. Qoidalarni qo'shing: til, cheklovlar, Claude nima qilmasligi kerak

Cowork'dan yordam so'rashingiz mumkin:
> "CLAUDE.md yaratishimga yordam ber. Men [kompaniya]da [lavozim] bo'lib ishlayman. Asosiy vazifalarim: [sanab o'ting]. To'liq fayl tuzish uchun menga aniqlashtiruvchi savollar ber."

Natijani tekshiring — Claude'ga oddiy vazifa bering va CLAUDE.md'dagi kontekstni ishlatayotganini ko'ring:
> "Haftalik hisobotim uchun shablon tayyorla"

Agar Claude lavozimingiz va formatga mos hisobot yaratsa — CLAUDE.md ishlayapti.

**3-topshiriq: "Oldin" Time Audit (3 daq)**

Time Audit — AI joriy etishdan oldin va keyin vazifalaringizga qancha vaqt ketayotganini o'lchash usuli. Busiz haqiqiy foydasini baholab bo'lmaydi.

**3-5 ta takrorlanuvchi ish vazifasini** tanlang va har biriga hozir qancha vaqt ketayotganini yozing:

| Vazifa | Chastotasi | Hozirgi vaqt |
|--------|-----------|-------------|
| Misol: Haftalik hisobot | Haftada 1 marta | 2 soat |
| Misol: Yig'ilishga tayyorgarlik | Haftada 2 marta | 40 daq |
| Misol: Ishga oid xat | Haftada 5 marta | 20 daq |
| ... | ... | ... |

Vazifa tanlash qoidalari:
- **Muntazam** bajariladigan vazifalar (kamida haftada bir marta)
- **Hujjat, jadval yoki matnlar** bilan bog'liq vazifalar (Claude bajara oladigan ishlar)
- Vaqtga halol yondashing — taxminiy emas, haqiqiy raqamlarni yozing

Bu jadvalni Google Sheets'da yarating — 5-modulda, tejashni o'lchaganimizda unga qaytamiz.

Cowork'dan yaratishni so'rashingiz mumkin:
> "Quyidagi ustunlar bilan 'Time Audit' Google Sheet yarat: Vazifa, Chastotasi, Oldingi vaqt, Keyingi vaqt, Tejash. Birinchi ustunni CLAUDE.md'dagi odatiy vazifalarim bilan to'ldir"

**Xavfsizlik: yakuniy tekshiruv**

Davom etishdan oldin ishonch hosil qiling:
- [ ] Google Workspace CLI orqali **ish** Google akkaunt ulangan (shaxsiy emas)
- [ ] Claude kirishi mumkin bo'lgan papkalarda mijozlarning shaxsiy ma'lumotlari yo'q
- [ ] Claude qaysi fayllarni ko'ra olishini tushunasiz

### Xulosa (30 sek)

Tabriklaymiz — AI-ofisingiz sozlandi. Sizda Google Workspace ulangan Claude Cowork, lavozimingiz konteksti yozilgan CLAUDE.md va haqiqiy raqamlar bilan "oldin" Time Audit bor. Keyingi modulda biz bu ofisdan hujjatlar yaratish uchun foydalanamiz — hisobotlar, xatlar va yig'ilish bayonnomalari to'g'ridan-to'g'ri Google Docs'da.

## Matnli qo'llanma

### AI-ofis sozlash cheklisti

2-modulga o'tishdan oldin barcha bandlarni bajaring:

**O'rnatish:**
- [ ] Claude Desktop Mac'ga o'rnatilgan
- [ ] Pro yoki Max obunasi faol
- [ ] Cowork varag'i mavjud

**Google Workspace CLI:**
- [ ] `gws` o'rnatilgan (`npm install -g @googleworkspace/cli`)
- [ ] `gws auth setup` bajarilgan
- [ ] `gws auth login` bajarilgan (Drive, Docs, Sheets)
- [ ] Claude Google Drive'dagi fayllarni ko'ra olyapti

**CLAUDE.md:**
- [ ] Fayl yaratilgan
- [ ] Lavozim va kompaniya ko'rsatilgan
- [ ] Odatiy vazifalar sanab o'tilgan
- [ ] Hujjat formati tavsiflangan
- [ ] Qoidalar va cheklovlar qo'shilgan

**Time Audit:**
- [ ] 3-5 ta takrorlanuvchi vazifa tanlangan
- [ ] Har biriga haqiqiy vaqt yozilgan
- [ ] Jadval Google Sheets'da yaratilgan

**Xavfsizlik:**
- [ ] Ish (shaxsiy emas) Google akkaunt ulangan
- [ ] Mavjud papkalarda shaxsiy ma'lumotli hujjatlar yo'q
- [ ] Claude bilan ishlash uchun alohida ish papkasi yaratilgan (tavsiya etiladi)

### Time Audit shabloni

Quyidagi tuzilma bilan Google Sheet yarating:

| Vazifa | Chastotasi | "Oldin" vaqti | "Keyin" vaqti | Tejash | Haftalik tejash |
|--------|-----------|--------------|--------------|--------|----------------|
| | | | _5-modulda to'ldiraimz_ | _avto_ | _avto_ |

**Time Audit uchun vazifalarni qanday tanlash:**

Mos keladi:
- Hisobotlar tayyorlash (haftalik, oylik)
- Ishga oid xatlar yozish
- Yig'ilishlarga tayyorgarlik
- Jadvallardagi ma'lumotlarni tahlil qilish
- Taqdimotlar yaratish
- Kiruvchi hujjatlarni qayta ishlash

Mos kelmaydi:
- Shaxsiy muloqot talab qiladigan vazifalar (muzokaralar, qo'ng'iroqlar)
- Yuqori noaniqlikdagi ijodiy vazifalar
- AI'ga yuklash mumkin bo'lmagan maxfiy ma'lumotli vazifalar

### Keyingi qadam

2-modulda siz sozlangan AI-ofisdan haqiqiy vazifalar uchun foydalanishni boshlaysiz:
- Google Docs'da hisobotlar yaratish
- Ishga oid xatlar
- Yig'ilish bayonnomalari

Bu vazifalarning barchasini Claude Google Workspace CLI orqali to'g'ridan-to'g'ri Google Docs'da bajaradi — nusxalashsiz.

## Asosiy xulosalar

1. **AI-ofis = Cowork + Google Workspace CLI + CLAUDE.md + Time Audit.** Samarali ishlash uchun to'rttala komponent kerak. `gws`siz — fayllarga kirish yo'q. CLAUDE.md'siz — kontekst yo'q. Time Audit'siz — o'lchanadigan natija yo'q
2. **"Oldin" Time Audit** joriy vazifalar vaqtini qayd qiladi. 5-modulda "keyin" vaqtini o'lchaysiz va daqiqalar hamda soatlardagi aniq tejashni ko'rasiz
3. **Xavfsizlik — formallik emas.** Ish akkauntni ulang, papkalarga kirishni nazorat qiling, mijozlarning shaxsiy ma'lumotlari bor hujjatlarni yuklamang

## Amaliy topshiriq

**Topshiriq:** To'liq AI-ofisni sozlash: Cowork + Google Workspace CLI + CLAUDE.md + "oldin" Time Audit

**Baholash mezonlari:**
- Claude Desktop o'rnatilgan, Cowork mavjud
- Google Workspace CLI ulangan, Claude Google Drive'dagi fayllarni ko'ra olyapti
- CLAUDE.md lavozimingiz konteksti bilan yaratilgan (kamida: siz kim ekansiz, vazifalar, format, qoidalar)
- "Oldin" Time Audit Google Sheets'da to'ldirilgan (3-5 ta vazifa, haqiqiy vaqt bilan)
- Xavfsizlik tekshiruvi o'tilgan (ish akkaunt, mavjud papkalarda shaxsiy ma'lumotlar yo'q)
