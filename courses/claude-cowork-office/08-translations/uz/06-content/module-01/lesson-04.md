# AI-ofisni sozlash / Dars 1.4: Amaliyot: o'z AI-ofisimizni sozlaymiz

## Metama'lumotlar

| Parametr | Qiymati |
|----------|----------|
| Modul | 1: AI-ofisni sozlash |
| Dars | 1.4 |
| Davomiyligi | 10 daq |
| Turi | Amaliyot |

## Video-skript

### Kirish (30 sek)

Oldingi darslarda biz nazariyani o'rgandik: agent chat-botdan nimasi bilan farq qiladi, Cowork'ni qanday o'rnatish va Google Workspace CLI'ni ulash, CLAUDE.md nima uchun kerak. Endi bularning hammasini amalda qilamiz. Bu darsda siz AI-ofisingizni sozlaysiz va Time Audit «oldin»ni to'ldirasiz — hozirgi vazifalaringizga qancha vaqt sarflanishini qayd qilasiz.

### Asosiy qism

**Topshiriq 1: O'rnatishni tekshiring (2 daq)**

Claude Desktop'ni oching va cheklist bo'yicha tekshirib chiqing:

- [ ] Claude Desktop o'rnatilgan va ishga tushirilgan
- [ ] Cowork varag'i mavjud
- [ ] Google Workspace CLI ulangan (Claude Google Drive'dagi fayllaringizni ko'radi)

Agar Google Workspace CLI hali sozlanmagan bo'lsa — 1.2-darsga qayting va qadamlarni bajaring. Usiz kursning qolgan modullari ishlamaydi.

Ulanishni tekshiring — Cowork'da yozing:
> «Google Drive'dagi fayllarim ro'yxatini ko'rsat»

Claude fayllaringiz ro'yxatini qaytarishi kerak.

**Topshiriq 2: CLAUDE.md yarating (5 daq)**

O'z lavozimingiz uchun CLAUDE.md yarating. 1.3-darsdagi shablondan foydalaning:

1. Siz kim ekanligizni tasvirlang: lavozim, bo'lim, kompaniya
2. Har hafta bajaradigan 4-5 ta odatiy vazifani sanab o'ting
3. Kompaniyangizda qabul qilingan hujjat formatini ko'rsating
4. Qoidalarni qo'shing: til, cheklovlar, Claude nima qilmasligi kerak

Cowork'dan yordam so'rashingiz mumkin:
> «CLAUDE.md yaratishga yordam ber. Men [kompaniya]da [lavozim] bo'lib ishlayman. Asosiy vazifalarim: [sanab o'ting]. To'liq fayl tuzish uchun aniqlashtiruvchi savollar ber.»

Natijani tekshiring — Claude'ga oddiy vazifa bering va CLAUDE.md'dagi kontekstdan foydalanyaptimi, ko'ring:
> «Haftalik hisobotim uchun shablon tayyorla»

Agar Claude lavozimingizga va formatga mos hisobot yaratsa — CLAUDE.md ishlayapti.

**Topshiriq 3: Time Audit «oldin» (3 daq)**

Time Audit — AI joriy qilishdan oldin va keyin vazifalarga qancha vaqt sarflashingizni o'lchash usuli. Busiz haqiqiy foydasini baholay olmaysiz.

**3-5 ta takrorlanuvchi ish vazifasini** tanlang va har biri hozir qancha vaqt olishini yozib qo'ying:

| Vazifa | Chastotasi | Hozirgi vaqt |
|--------|-----------|-------------|
| Masalan: Haftalik hisobot | Haftada 1 marta | 2 soat |
| Masalan: Yig'ilishga tayyorgarlik | Haftada 2 marta | 40 daq |
| Masalan: Ishga oid xat | Haftada 5 marta | 20 daq |
| ... | ... | ... |

Vazifalarni tanlash qoidalari:
- **Muntazam** bajaradigan vazifalar (kamida haftada bir marta)
- **Hujjatlar, jadvallar yoki matnlar** bilan bog'liq vazifalar (Claude bajara oladigan narsalar)
- Vaqtga chinakamiga to'g'ri baho bering — haqiqiy raqamlarni yozing, taxminiy emas

Bu jadvalni Google Sheets'da yarating — 5-modulda tejashni o'lchaganimizda unga qaytamiz.

Cowork'dan yaratishni so'rashingiz mumkin:
> «"Time Audit" nomli Google Sheet yarat, ustunlari: Vazifa, Chastotasi, Oldingi vaqt, Keyingi vaqt, Tejash. Birinchi ustunni CLAUDE.md'dagi odatiy vazifalarim bilan to'ldir»

**Xavfsizlik: yakuniy tekshiruv**

Davom etishdan oldin ishonch hosil qiling:
- [ ] Google Workspace CLI orqali **ish** Google akkaunt ulangan (shaxsiy emas, oilaviy fotosuratlar bor emas)
- [ ] Claude ko'radigan papkalarda mijozlarning shaxsiy ma'lumotlari bor hujjatlar yo'q
- [ ] Siz Claude qaysi fayllarni ko'ra olishini tushunasiz

### Xulosa (30 sek)

Tabriklaymiz — AI-ofisingiz sozlandi. Sizda Google Workspace ulangan Claude Cowork, lavozimingiz konteksti bilan CLAUDE.md va haqiqiy raqamlar bilan Time Audit «oldin» bor. Keyingi modulda biz bu ofisdan hujjatlar yaratish uchun foydalana boshlaymiz — hisobotlar, xatlar va yig'ilish bayonnomalari bevosita Google Docs'da.

## Matnli qo'llanma

### AI-ofis sozlash cheklisti

2-modulga o'tishdan oldin barcha bandlarni bajaring:

**O'rnatish:**
- [ ] Claude Desktop Mac'ga o'rnatilgan
- [ ] Pro yoki Max obuna faol
- [ ] Cowork varag'i mavjud

**Google Workspace CLI:**
- [ ] `gws` o'rnatilgan (`npm install -g @googleworkspace/cli`)
- [ ] `gws auth setup` bajarilgan
- [ ] `gws auth login` bajarilgan (Drive, Docs, Sheets)
- [ ] Claude Google Drive'dagi fayllarni ko'radi

**CLAUDE.md:**
- [ ] Fayl yaratilgan
- [ ] Lavozim va kompaniya ko'rsatilgan
- [ ] Odatiy vazifalar sanab o'tilgan
- [ ] Hujjat formati tasvirlangan
- [ ] Qoidalar va cheklovlar qo'shilgan

**Time Audit:**
- [ ] 3-5 ta takrorlanuvchi vazifa tanlangan
- [ ] Har biri uchun haqiqiy vaqt yozilgan
- [ ] Jadval Google Sheets'da yaratilgan

**Xavfsizlik:**
- [ ] Ish (shaxsiy emas) Google akkaunt ulangan
- [ ] Kirish mumkin bo'lgan papkalarda shaxsiy ma'lumotli hujjatlar yo'q
- [ ] Claude uchun alohida ish papkasi yaratilgan (tavsiya etiladi)

### Time Audit shabloni

Quyidagi tuzilma bilan Google Sheet yarating:

| Vazifa | Chastotasi | Vaqt «oldin» | Vaqt «keyin» | Tejash | Haftalik tejash |
|--------|-----------|-------------|-------------|--------|-----------------|
| | | | _5-modulda to'ldiramiz_ | _avto_ | _avto_ |

**Time Audit uchun vazifalarni qanday tanlash:**

Mos keladi:
- Hisobotlar tayyorlash (haftalik, oylik)
- Ishga oid xatlar yozish
- Yig'ilishlarga tayyorgarlik
- Jadvallardagi ma'lumotlarni tahlil qilish
- Taqdimotlar yaratish
- Kiruvchi hujjatlarni qayta ishlash

Mos kelmaydi:
- Shaxsiy muloqat talab qiladigan vazifalar (muzokara, qo'ng'iroqlar)
- Yuqori noaniqlikdagi ijodiy vazifalar
- AI'ga yuklash mumkin bo'lmagan maxfiy ma'lumotli vazifalar

### Keyingi qadam

2-modulda siz sozlangan AI-ofisdan haqiqiy vazifalar uchun foydalana boshlaysiz:
- Google Docs'da hisobotlar yaratish
- Ishga oid xatlar
- Yig'ilish bayonnomalari

Bu vazifalarning hammasini Claude Google Workspace CLI orqali bevosita Google Docs'da bajaradi — nusxalashsiz.

## Asosiy xulosalar

1. **AI-ofis = Cowork + Google Workspace CLI + CLAUDE.md + Time Audit.** Samarali ishlash uchun to'rttala komponent kerak. `gws`'siz — fayllarga kirish yo'q. CLAUDE.md'siz — kontekst yo'q. Time Audit'siz — o'lchanadigan natija yo'q
2. **Time Audit «oldin»** hozirgi vazifalarga sarflanayotgan vaqtni qayd qiladi. 5-modulda «keyin» vaqtini o'lchaysiz va daqiqa va soatlarda aniq tejashni ko'rasiz
3. **Xavfsizlik — rasmiyatchilik emas.** Ish akkauntni ulang, papkalarga kirishni nazorat qiling, mijozlarning shaxsiy ma'lumotlari bor hujjatlarni yuklamang

## Amaliy topshiriq

**Topshiriq:** To'liq AI-ofisni sozlash: Cowork + Google Workspace CLI + CLAUDE.md + Time Audit «oldin»

**Bajarish mezonlari:**
- Claude Desktop o'rnatilgan, Cowork mavjud
- Google Workspace CLI ulangan, Claude Google Drive'dagi fayllarni ko'radi
- CLAUDE.md lavozimingiz konteksti bilan yaratilgan (kamida: siz kim, vazifalar, format, qoidalar)
- Time Audit «oldin» Google Sheets'da to'ldirilgan (3-5 ta vazifa, haqiqiy vaqt bilan)
- Xavfsizlik tekshiruvi o'tgan (ish akkaunt, kirish mumkin bo'lgan papkalarda shaxsiy ma'lumotlar yo'q)
