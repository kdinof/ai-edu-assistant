# Test: AI-ofisni sozlash / Dars 1.1: Chat-bot va agent

## Metama'lumotlar

| Parametr | Qiymat |
|----------|--------|
| Modul | 1: AI-ofisni sozlash |
| Dars | 1.1 |
| Savollar soni | 4 |
| O'tish bali | 70% |

## Savollar

### Savol 1

**Turi:** scenario

Sizga haftalik sotuv hisobotini tayyorlash kerak. Ma'lumotlar Google Sheets'da, tayyor hisobot esa Google Docs'da bo'lishi kerak. Siz ChatGPT'ni ochasiz va jadvaldan ma'lumotlarni chatga ko'chirasiz. Bu yondashuvda nima noto'g'ri?

- A) Siz nusxalash va qo'lda formatlashga vaqt sarflayapsiz, holbuki agent bularning hammasini avtomatik qila oladi
- B) ChatGPT jadvallarni tahlil qila olmaydi — maxsus vosita ishlatish kerak
- C) Ish ma'lumotlarini chat-botga ko'chirish xavfsiz emas
- D) ChatGPT sifatsiz hisobot qiladi — Claude ishlatish kerak

**To'g'ri javob:** A
**Izoh:** Chat-botning asosiy muammosi — yaratish atrofidagi qo'l mehnati: ma'lumotlarni nusxalash, matnni hujjatga ko'chirish, formatlash. Agent (Cowork + Google Workspace CLI) vazifani to'liq bajaradi — ma'lumotlarni o'qishdan tayyor hujjatni saqlashgacha.

---

### Savol 2

**Turi:** single_choice

Google Workspace CLI (`gws`) Claude Cowork bilan birgalikda nima qiladi?

- A) Google Workspace'ni almashtiradi — Claude Google akkauntsiz fayllar bilan ishlaydi
- B) Google Drive va kompyuter o'rtasida fayllarni sinxronlaydi, Dropbox kabi
- C) Claude yaratgan matnlar sifatini avtomatik yaxshilaydi
- D) Claude'ga Google Docs, Sheets va Drive'dagi fayllarni bevosita o'qish va yaratish imkonini beradi

**To'g'ri javob:** D
**Izoh:** `gws` — Claude va Google Workspace o'rtasidagi ko'prik. Usiz Claude faqat chat oynasida matn yarata oladi. U bilan esa — jadvallarni o'qiydi, hujjatlar yaratadi va fayllarni Google Drive'ga saqlaydi.

---

### Savol 3

**Turi:** find_error

Hamkasbingiz Cowork'dan qanday foydalanishini aytib beryapti: "Men Cowork'ga 'Sotuvlar bo'yicha hisobot matni yoz' deb yozaman, natijani ko'chiraman, Google Docs'ga qo'yaman, jadvalni formatlaymanman va rahbarga jo'nataman. Cowork — zo'r narsa, vaqtni tejaydi!" Bu yerda nima noto'g'ri?

- A) Hisobotni avval rahbarga tekshirtirib, keyin jo'natish kerak
- B) Cowork o'rniga ChatGPT ishlatish kerak — u hisobotlarni yaxshiroq yozadi
- C) Hamkasbingiz Cowork'dan chat-bot sifatida foydalanyapti — hujjatni to'liq yaratish vazifasini qo'yish o'rniga matnni nusxalab olyapti
- D) Hamkasbingiz davrni ko'rsatmagan — "mart oyi uchun sotuv hisoboti" deb yozish kerak edi

**To'g'ri javob:** C
**Izoh:** Asosiy xato — Cowork'dan oddiy chat-bot sifatida foydalanish. To'g'ri yondashuv: vazifani to'liq berish — "Google Sheets'dan ma'lumotlarni ol, Google Docs'da hisobot yarat, 'Hisobotlar' papkasiga saqlа". Cowork hammasini o'zi Google Workspace CLI orqali bajaradi.

---

### Savol 4

**Turi:** scenario

Siz — Uzum kompaniyasida marketologsiz. Haftalik reklama kampaniyalari hisobotini tayyorlashingiz kerak. Ma'lumotlar Google Sheets'da, hisobot Google Docs'da kerak. Cowork uchun qaysi topshiriq eng samarali bo'ladi?

- A) "Hafta uchun reklama hisobotini yoz"
- B) "Google Sheets'dagi 'Reklama_mart_2026' jadvalidan ma'lumotlarni ol, so'nggi hafta natijalarini tahlil qil. 'Marketing' papkasidagi Google Docs'da hisobot yarat: ko'rsatkichlar jadvali (CTR, CPA, byudjet), o'tgan hafta bilan taqqoslash, 3 ta tavsiya"
- C) "Reklama ma'lumotlarini tahlil qilib, nimani yaxshilash mumkinligini ayt"
- D) "Reklama ma'lumotlari jadvalini och. Keyin hujjat yarat. Keyin unga hisobot yoz."

**To'g'ri javob:** B
**Izoh:** Samarali topshiriq freymvorkning barcha 4 elementini o'z ichiga oladi: Nima (ko'rsatkichlar va tavsiyalar bilan hisobot) - Qayerdan (Google Sheets) - Qayerga (Google Docs, papka) - Format (jadval + taqqoslash + tavsiyalar). Qolgan variantlar yoki juda noaniq, yoki bitta topshiriq o'rniga vazifani mayda qadamlarga bo'lib tashlaydi.
