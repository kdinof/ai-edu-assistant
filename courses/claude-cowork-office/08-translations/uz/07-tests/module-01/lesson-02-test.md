# Test: AI-ofisni sozlash / Dars 1.2: Cowork + Google Workspace CLI o'rnatish va sozlash

## Metama'lumotlar

| Parametr | Qiymati |
|----------|----------|
| Modul | 1: AI-ofisni sozlash |
| Dars | 1.2 |
| Savollar soni | 4 |
| O'tish bali | 70% |

## Savollar

### Savol 1

**Turi:** single_choice

Claude Cowork'dan foydalanmoqchisiz. Buning uchun minimal qanday obuna kerak?

- A) Bepul Claude rejasi — Cowork hammaga ochiq
- B) Claude Pro ($20/oy) — Cowork obunaga kiritilgan
- C) Claude Max ($100/oy) — Cowork faqat eng yuqori tarifda mavjud
- D) Obuna kerak emas — Claude Desktop'ni o'rnatish yetarli

**To'g'ri javob:** B
**Izoh:** Cowork Claude Pro ($20/oy) obunasidan boshlab mavjud. Bepul rejada agent rejimi ochiq emas. Max ($100/oy) ham mos, lekin u minimal zaruriy emas.

---

### Savol 2

**Turi:** scenario

Siz Claude Desktop va Google Workspace CLI'ni o'rnatdingiz. Claude fayllaringizni ko'rayotganini tekshirmoqchisiz. Qaysi amal ulanish ishlayotganini tasdiqlaydi?

- A) Brauzerda Google Drive'ni ochib, fayllar joyida ekanini tekshirish
- B) Claude Desktop'ni qayta ishga tushirish — agar xatolar bo'lmasa, hammasi ishlayapti
- C) Terminal'da `gws --version` bajarib, versiya ko'rinishiga ishonch hosil qilish
- D) Claude Desktop (Cowork)'da «Google Drive'dagi fayllarimni ko'rsat» deb yozib, Claude fayllar ro'yxatini qaytarishiga ishonch hosil qilish

**To'g'ri javob:** D
**Izoh:** Versiyani tekshirish (C) faqat `gws` o'rnatilganini tasdiqlaydi, lekin Google akkauntga ulanishni emas. Brauzer orqali tekshirish (A) Claude fayllarni ko'rayotganini ko'rsatmaydi. Butun zanjirni tekshirish kerak: Claude → gws → Google Drive.

---

### Savol 3

**Turi:** multiple_choice

Google Workspace CLI orqali Claude'ga qaysi ma'lumotlarni ulash xavfsiz? (3 ta to'g'ri javobni tanlang)

- A) Jamlangan ma'lumotli ish hisobotlari
- B) Mijozlarning shaxsiy ma'lumotlari bor jadval (ism + pasport ma'lumotlari)
- C) Kompaniyaning hujjat shablonlari
- D) Parollar va kirish kalitlari bor fayl
- E) Ishga oid xatlarning qoralama nusxalari

**To'g'ri javob:** A, C, E
**Izoh:** Shaxsiy ma'lumotlarsiz ish hujjatlarini ulash xavfsiz: hisobotlar, shablonlar, qoralama nusxalar. Mijozlarning shaxsiy ma'lumotlari va parollarni ulash mumkin emas — bu maxfiy ma'lumotlarning sizib chiqish xavfi.

---

### Savol 4

**Turi:** find_error

Hamkasbingiz Google Workspace CLI'ni sozlab, Claude'ga shaxsiy Google akkauntini ulagan — unda oilaviy suratlar, shaxsiy yozishmalar va ish fayllari bitta papkada saqlanadi. «Akkauntlar o'rtasida almashib o'tirish shart emas!» — deydi u. Muammo nimada?

- A) Claude barcha fayllarga, jumladan shaxsiy fayllarga kirish huquqini oladi — ish akkauntni ulab, AI bilan ishlash uchun alohida papka yaratish yaxshiroq
- B) Shaxsiy akkaunt korporativ Google Workspace'dan sekinroq ishlaydi
- C) Claude shaxsiy Google akkauntlarni qo'llab-quvvatlamaydi — Google Workspace kerak
- D) Bepul Google akkauntda API so'rovlar soni cheklangan

**To'g'ri javob:** A
**Izoh:** `gws` orqali Claude ulangan akkauntdagi fayllarni ko'radi. Agar bu shaxsiy ma'lumotlari bor shaxsiy akkaunt bo'lsa — Claude ularga kirishga ega bo'ladi. Tavsiya: ish akkauntni ulash va AI bilan ishlash uchun alohida papka yaratish.
