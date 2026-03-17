# Test: AI-ofisni sozlash / Dars 1.2: Cowork + Google Workspace CLI o'rnatish va sozlash

## Metama'lumotlar

| Parametr | Qiymat |
|----------|--------|
| Modul | 1: AI-ofisni sozlash |
| Dars | 1.2 |
| Savollar soni | 4 |
| O'tish bali | 70% |

## Savollar

### Savol 1

**Turi:** single_choice

Siz Claude Cowork'dan foydalanmoqchisiz. Buning uchun eng kam qaysi obuna kerak?

- A) Bepul Claude rejasi — Cowork hammaga ochiq
- B) Claude Pro ($20/oy) — Cowork obunaga kiritilgan
- C) Claude Max ($100/oy) — Cowork faqat eng yuqori tarifda mavjud
- D) Obuna kerak emas — Claude Desktop'ni o'rnatish yetarli

**To'g'ri javob:** B
**Izoh:** Cowork Claude Pro obunasidan ($20/oy) boshlab mavjud. Bepul rejada agent rejimi mavjud emas. Max ($100/oy) ham mos keladi, lekin eng kam zaruriy emas.

---

### Savol 2

**Turi:** scenario

Siz Claude Desktop va Google Workspace CLI'ni o'rnatdingiz. Claude fayllaringizni ko'rayotganini tekshirmoqchisiz. Qaysi amal ulanish ishlayotganini tasdiqlaydi?

- A) Brauzerda Google Drive'ni ochib, fayllar joyida ekanini tekshirish
- B) Claude Desktop'ni qayta ishga tushirish — agar xato bo'lmasa, hammasi ishlayapti
- C) Terminal'da `gws --version` buyrug'ini bajarib, versiya ko'rsatilishini tekshirish
- D) Claude Desktop'da (Cowork) "Google Drive'dagi fayllarimni ko'rsat" deb yozib, Claude fayllar ro'yxatini qaytarishini tekshirish

**To'g'ri javob:** D
**Izoh:** Versiyani tekshirish (C) faqat `gws` o'rnatilganini tasdiqlaydi, Google akkauntga ulanishni emas. Brauzerda tekshirish (A) Claude'ning fayllarni ko'rayotganini ko'rsatmaydi. Butun zanjirni tekshirish kerak: Claude - gws - Google Drive.

---

### Savol 3

**Turi:** multiple_choice

Google Workspace CLI orqali Claude'ga qanday ma'lumotlarni ulash xavfsiz? (3 ta to'g'ri javobni tanlang)

- A) Umumlashtirilgan ma'lumotli ish hisobotlari
- B) Mijozlarning shaxsiy ma'lumotlari bor jadval (ism + pasport ma'lumotlari)
- C) Kompaniya hujjat shablonlari
- D) Parollar va kirish kalitlari fayli
- E) Ishga oid xat qoralmalari

**To'g'ri javob:** A, C, E
**Izoh:** Shaxsiy ma'lumotlarsiz ish hujjatlarini ulash xavfsiz: hisobotlar, shablonlar, qoralamalar. Mijozlarning shaxsiy ma'lumotlari va parollarni ulash mumkin emas — bu maxfiy ma'lumotlar oqib chiqishi xavfini tug'diradi.

---

### Savol 4

**Turi:** find_error

Hamkasbingiz Google Workspace CLI'ni sozlab, Claude'ga oilaviy fotosuratlar, shaxsiy yozishmalar va ish fayllari bitta papkada saqlanadigan shaxsiy Google akkauntini ulagan. "Akkauntlar o'rtasida almashish shart emas!" — deydi u. Muammo nimada?

- A) Claude barcha fayllarga, jumladan shaxsiy fayllarga ham kirish huquqiga ega bo'ladi — ish akkauntni ulab, AI bilan ishlash uchun alohida papka yaratish yaxshiroq
- B) Shaxsiy akkaunt korporativ Google Workspace'dan sekinroq ishlaydi
- C) Claude shaxsiy Google akkauntlarni qo'llab-quvvatlamaydi — Google Workspace kerak
- D) Bepul Google akkauntda API so'rovlari cheklangan

**To'g'ri javob:** A
**Izoh:** `gws` orqali Claude ulangan akkauntdagi fayllarni ko'radi. Agar bu shaxsiy ma'lumotlar bilan shaxsiy akkaunt bo'lsa — Claude ularga ham kirish huquqiga ega bo'ladi. Tavsiya: ish akkauntni uling va AI bilan ishlash uchun alohida papka yarating.
