# Test: Avtomatlashtirish va natija / Dars 5.2: Murakkab skill'lar va avtomatlashtirish

## Metama'lumotlar

| Parametr | Qiymat |
|----------|--------|
| Modul | 5: Avtomatlashtirish va natija |
| Dars | 5.2 |
| Savollar soni | 4 |
| O'tish bali | 70% |

## Savollar

### Savol 1

**Turi:** single_choice

Murakkab skill oddiy skill'dan nimasi bilan farq qiladi?

- A) Murakkab skill boshqa fayl formatidan foydalanadi
- B) Murakkab skill bir necha bosqichli zanjirdan iborat, har bir bosqich natijasi keyingisiga uzatiladi
- C) Murakkab skill faqat Google Sheets bilan ishlaydi, oddiy skill esa har qanday vosita bilan
- D) Murakkab skill foydalanish uchun qimmatroq

**To'g'ri javob:** B
**Izoh:** Murakkab skill — qayta foydalanish uchun saqlangan pipeline. U zanjirda 2-4 ta vazifani o'z ichiga oladi (masalan: Sheets dan ma'lumotlar → Docs da hisobot → Slides da taqdimot). Texnik jihatdan bu xuddi shu skill, lekin ko'rsatmada bir necha bosqich bilan.

---

### Savol 2

**Turi:** scenario

Siz har dushanba soat 9:00 da Cowork avtomatik ravishda rejalashtiruvga kun tartibini tayyorlashini xohlaysiz. Scheduled task sozladingiz. Lekin dushanba ertalab Mac soat 9:30 gacha uyqu rejimida edi. Nima bo'ladi?

- A) Cowork vazifani bulutda bajaradi va Mac ni ochganingizda natijani ko'rsatadi
- B) Vazifa o'tkazib yuboriladi — scheduled tasks faqat Mac yoqilgan va Claude Desktop ochiq bo'lganda ishlaydi
- C) Cowork sizga bildirishnoma yuboradi va Mac uyg'onganda vazifani bajaradi
- D) Vazifa ertasi kuni soat 9:00 da bajariladi

**To'g'ri javob:** B
**Izoh:** Scheduled tasks — lokal avtomatlashtirish, bulutli xizmat emas. Agar Mac uyqu rejimida yoki Claude Desktop yopiq bo'lsa — vazifa o'tkazib yuboriladi. Amaliy maslahat: ertalabki vazifalar uchun Mac va Claude Desktop kerakli vaqtdan oldin ishga tushirilganligiga ishonch hosil qiling yoki skill'ni qo'lda ishga tushiring.

---

### Savol 3

**Turi:** find_error

Hamkasbingiz 12 bosqichli «To'liq ish kuni» nomli bitta skill yaratdi: ertalabki hisobot, pochtani tekshirish, jadval tahlili, mijozlarga 3 ta xat, uchrashuvga tayyorgarlik, bayonnoma, kechki xulosa, trekkerni yangilash, hisobot yuborish, zaxira nusxa olish. Nima noto'g'ri?

- A) Cowork'da bosqichlar soniga cheklov yo'q — shundayligicha qoldirish mumkin
- B) Skill juda murakkab — 3-4 ta alohida skill'ga ajratish yaxshiroq (ertalabki, uchrashuv uchun, kechki), ularni ishga tushirish va sozlash osonroq
- C) Barcha ish vazifalarini qamrab olish uchun yana bosqichlar qo'shish kerak
- D) Skill faqat bitta bosqichdan iborat bo'lishi kerak — murakkab skill'lar qo'llab-quvvatlanmaydi

**To'g'ri javob:** B
**Izoh:** 10+ bosqichli skill'ni sozlash juda qiyin — bitta bosqich noto'g'ri natija bersa, tuzatish uzoq davom etadi. 2-3 ta alohida skill'ga ajratish yaxshiroq (ertalabki, uchrashuv uchun, kechki). Ikkita skill'ni ketma-ket ishga tushirish, bitta juda murakkab skill'ni sozlashdan osonroq.

---

### Savol 4

**Turi:** single_choice

CLAUDE.md va skill'lar o'rtasida ma'lumotni qanday to'g'ri taqsimlash kerak?

- A) Hammasini CLAUDE.md ga yozish — skill'lar kerak emas
- B) CLAUDE.md — kontekst (lavozim, qoidalar, hujjat formati), skill'lar — vazifalar uchun aniq ko'rsatmalar
- C) CLAUDE.md — shaxsiy eslatmalar uchun, skill'lar — ish vazifalari uchun
- D) Ishonchlilik uchun ma'lumotni ikkala joyda ham takrorlash

**To'g'ri javob:** B
**Izoh:** CLAUDE.md va skill'lar bir-birini to'ldiradi: CLAUDE.md kontekstni saqlaydi (siz kim ekansiz, kompaniya qoidalari, hujjat formati), skill'lar esa — vazifalarni bajarishning aniq bosqichlari. Cowork ikkalasidan foydalanadi: CLAUDE.md dan kontekstni, skill'dan ko'rsatmalarni oladi. Takrorlash shart emas.
