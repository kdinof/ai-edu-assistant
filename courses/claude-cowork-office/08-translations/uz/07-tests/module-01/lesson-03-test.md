# Test: AI-ofisni sozlash / Dars 1.3: CLAUDE.md: lavozimingiz konteksti

## Metama'lumotlar

| Parametr | Qiymati |
|----------|----------|
| Modul | 1: AI-ofisni sozlash |
| Dars | 1.3 |
| Savollar soni | 4 |
| O'tish bali | 70% |

## Savollar

### Savol 1

**Turi:** scenario

Siz — Toshkentdagi qurilish kompaniyasida buxgaltersiz. Sizda lavozim va vazifalar tasvirlangan CLAUDE.md bor. Siz Cowork'ga «Haftalik hisobotni tayyorla» deb yozasiz. Hamkasbingiz-marketolog ham «Haftalik hisobotni tayyorla» deb yozadi, lekin uning o'z CLAUDE.md'si bor. Nima sodir bo'ladi?

- A) Ikkisi ham bir xil universal hisobot shablonini oladi
- B) Claude ikkalasidan ham «Qanday hisobot?» deb so'raydi, chunki so'rov aniq emas
- C) Claude ikkalasini ham rad etadi, chunki ma'lumot manbasi ko'rsatilmagan
- D) Siz xarajatlar bo'yicha jadvalli hisobot olasiz, hamkasbingiz esa CTR va CPA ko'rsatkichlari bilan reklama kampaniyalari hisobotini oladi, chunki Claude CLAUDE.md'dagi kontekstdan foydalanadi

**To'g'ri javob:** D
**Izoh:** CLAUDE.md lavozim kontekstini o'z ichiga oladi: vazifalar, hujjat formati, qoidalar. Claude undan avtomatik foydalanadi va natijani aniq lavozimga mos ravishda shakllantiradi — bir xil so'rovda ham.

---

### Savol 2

**Turi:** multiple_choice

Ofis xodimi uchun CLAUDE.md'ga nimalarni kiritish kerak? (3 ta to'g'ri javobni tanlang)

- A) Tezkor kirish uchun ish servislarining parollari
- B) Lavozim, bo'lim va kompaniya
- C) Har hafta bajaradigan odatiy vazifalar
- D) Kompaniyada qabul qilingan hujjat formati
- E) Yillik shaxsiy maqsadlar va karyera o'sish rejasi

**To'g'ri javob:** B, C, D
**Izoh:** CLAUDE.md ish kontekstini o'z ichiga olishi kerak: siz kim (B), nima qilasiz (C), hujjatlarni qanday rasmiylashtirasiz (D). Parollarni CLAUDE.md'da saqlash mumkin emas — bu ochiq matn fayli. Shaxsiy maqsadlar Claude'ga ish vazifalarini yaxshiroq bajarishga yordam bermaydi.

---

### Savol 3

**Turi:** find_error

Loyiha menejeri quyidagi mazmundagi CLAUDE.md yaratgan:

```
# CLAUDE.md
Salom, Claude! Sen mening yordamchimsan. Ishda yordam ber. Hammasini yaxshi qil.
```

Bu CLAUDE.md'da nima noto'g'ri?

- A) Claude'ga «sen» deb murojaat qilish mumkin emas — rasmiy uslub kerak
- B) CLAUDE.md juda qisqa — kamida 500 so'z kerak
- C) Faylda aniqlik yo'q: lavozim, vazifalar, hujjat formati va qoidalar ko'rsatilmagan — Claude foydali kontekst olmaydi
- D) Sarlavhalar va ro'yxatlar bilan Markdown-formatlashni ishlatish shart

**To'g'ri javob:** C
**Izoh:** «Hammasini yaxshi qil» — bu ko'rsatma emas. Aniq kontekstsiz (lavozim, vazifalar, format) Claude universal AI bo'lib qoladi va ishni rolingizga moslashtirolmaydi. Natija — xuddi CLAUDE.md umuman bo'lmagandek.

---

### Savol 4

**Turi:** scenario

Sizda CLAUDE.md yo'q. Har safar Claude'dan hisobot yaratishni so'raganingizda yozasiz: «Men Toshkentdagi Vertex kompaniyasida buxgalterman. Hisobot formati: jadval + 3 ta xulosa. Til — o'zbek. Ma'lumotni ... dan ol.» Nimani yaxshilash mumkin?

- A) Takrorlanuvchi kontekstni (lavozim, format, qoidalar) CLAUDE.md'ga ko'chirish — shunda faqat vazifaning mohiyatini yozish kifoya bo'ladi
- B) Hech narsa — bu to'g'ri yondashuv, har safar kontekstni ko'rsatish kerak
- C) Bu matnni vaqtinchalik xotiraga saqlash va har so'rov oldidan joylashtirish
- D) Claude'dan bu ma'lumotni bir marta eslab qolishni so'rash — u keyingi chatlarda eslab qoladi

**To'g'ri javob:** A
**Izoh:** CLAUDE.md har ishga tushirilganda avtomatik yuklanadi. Har so'rovda kontekstni takrorlash o'rniga uni bir marta yozasiz — va Claude har doim undan foydalanadi. Bir marta 10 daqiqa sarflang — har murojaat qilganingizda tejaysiz.
