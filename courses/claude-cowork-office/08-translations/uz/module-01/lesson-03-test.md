# Test: AI-ofisni sozlash / Dars 1.3: CLAUDE.md: lavozimingiz konteksti

## Metama'lumotlar

| Parametr | Qiymat |
|----------|--------|
| Modul | 1: AI-ofisni sozlash |
| Dars | 1.3 |
| Savollar soni | 4 |
| O'tish bali | 70% |

## Savollar

### Savol 1

**Turi:** scenario

Siz — Toshkentdagi qurilish kompaniyasida buxgaltersiz. Sizda lavozim va vazifalar tavsiflangan CLAUDE.md bor. Cowork'ga yozasiz: "Haftalik hisobot tayyorla". Hamkasbingiz marketolog ham "Haftalik hisobot tayyorla" deb yozadi, lekin uning o'zining CLAUDE.md'si bor. Nima bo'ladi?

- A) Ikkalasi ham bir xil universal hisobot shablonini oladi
- B) Claude ikkalasidan ham "Qanday hisobot?" deb so'raydi, chunki so'rov noaniq
- C) Claude ikkalasiga ham rad javobini beradi, chunki ma'lumot manbai ko'rsatilmagan
- D) Siz jadval bilan xarajatlar hisobotini olasiz, hamkasbingiz esa CTR va CPA ko'rsatkichlari bilan reklama kampaniyalari hisobotini oladi, chunki Claude CLAUDE.md'dagi kontekstni ishlatadi

**To'g'ri javob:** D
**Izoh:** CLAUDE.md lavozim kontekstini o'z ichiga oladi: vazifalar, hujjat formati, qoidalar. Claude uni avtomatik ishlatadi va natijani aniq lavozimga moslaydi — bir xil so'rov bo'lsa ham.

---

### Savol 2

**Turi:** multiple_choice

Ofis xodimi uchun CLAUDE.md'ga nimalarni kiritish kerak? (3 ta to'g'ri javobni tanlang)

- A) Ish xizmatlariga parollar — tez kirish uchun
- B) Lavozim, bo'lim va kompaniya
- C) Har hafta bajaradigan odatiy vazifalar
- D) Kompaniyada qabul qilingan hujjat formati
- E) Yillik shaxsiy maqsadlar va martaba o'sish rejasi

**To'g'ri javob:** B, C, D
**Izoh:** CLAUDE.md ish kontekstini o'z ichiga olishi kerak: siz kim ekansiz (B), nima qilasiz (C), hujjatlarni qanday rasmiylashtirasiz (D). Parollarni CLAUDE.md'da saqlash mumkin emas — bu ochiq matnli fayl. Shaxsiy maqsadlar Claude'ga ish vazifalarini yaxshiroq bajarishga yordam bermaydi.

---

### Savol 3

**Turi:** find_error

Loyiha menejeri quyidagi mazmun bilan CLAUDE.md yaratdi:

```
# CLAUDE.md
Salom, Claude! Sen mening yordamchimsan. Ishimda yordam ber. Hammasini yaxshi qil.
```

Bu CLAUDE.md'da nima noto'g'ri?

- A) Claude'ga "sen" deb murojaat qilish mumkin emas — rasmiy uslub kerak
- B) CLAUDE.md juda qisqa — kamida 500 so'z bo'lishi kerak
- C) Faylda aniqlik yo'q: lavozim, vazifalar, hujjat formati va qoidalar ko'rsatilmagan — Claude foydali kontekst olmayapti
- D) Markdown formatlashdan sarlavhalar va ro'yxatlar bilan foydalanish shart

**To'g'ri javob:** C
**Izoh:** "Hammasini yaxshi qil" — bu ko'rsatma emas. Aniq kontekstsiz (lavozim, vazifalar, format) Claude universal AI bo'lib qoladi va ishni sizning rolingizga moslay olmaydi. Natija — CLAUDE.md umuman bo'lmaganidek.

---

### Savol 4

**Turi:** scenario

Sizda CLAUDE.md yo'q. Har safar Claude'dan hisobot yaratishni so'raganingizda yozasiz: "Men Toshkentdagi Vertex kompaniyasida buxgalterman. Hisobot formati: jadval + 3 ta xulosa. Til — o'zbek. Ma'lumotlarni ... dan ol". Nimani yaxshilash mumkin?

- A) Takrorlanuvchi kontekstni (lavozim, format, qoidalar) CLAUDE.md'ga ko'chirish — shunda faqat vazifaning mohiyatini yozish yetarli bo'ladi
- B) Hech narsa — bu to'g'ri yondashuv, har safar kontekstni ko'rsatish kerak
- C) Bu matnni vaqtinchalik xotiraga saqlab, har safar so'rovdan oldin qo'yib qo'yish kerak
- D) Claude'dan bu ma'lumotni bir marta eslab qolishini so'rash kerak — keyingi chatlarda eslab qoladi

**To'g'ri javob:** A
**Izoh:** CLAUDE.md har safar ishga tushganda avtomatik yuklanadi. Har so'rovda kontekstni takrorlash o'rniga, uni bir marta yozasiz — va Claude har safar foydalanadi. Bir marta 10 daqiqa sarflang — har safar murojaat qilganingizda tejaysiz.
