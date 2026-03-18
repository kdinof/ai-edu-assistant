# Test: Taqdimotlar va payplaynlar / Dars 4.1: Claude orqali taqdimotlar

## Metama'lumotlar

| Parametr | Qiymati |
|----------|----------|
| Modul | 4: Taqdimotlar va payplaynlar |
| Dars | 4.1 |
| Savollar soni | 4 |
| O'tish bali | 70% |

## Savollar

### Savol 1

**Turi:** single_choice

Siz rahbar bilan haftalik uchrashuv uchun choraklik hisobot taqdimotini tayyorlashingiz kerak. Taqdimot yaratishning qaysi yondashuvi optimal?

- A) PPTX — code execution orqali — dizayn ustidan maksimal nazorat uchun
- B) Google Slides — Google Workspace CLI orqali — tez, darhol brauzerda mavjud
- C) Google Slides'da slaydlarni qo'lda yaratish — Cowork taqdimotlar bilan ishlay olmaydi
- D) Taqdimot o'rniga tezislar bilan PDF yaratish

**To'g'ri javob:** B
**Izoh:** Ish taqdimotlari uchun (rahbarga hisobot, uchrashuv kun tartibi) Google Slides — gws orqali optimal: fayl darhol Google Drive'da, birgalikda tahrirlash mumkin, hech narsa yuklab olish shart emas. PPTX — code execution orqali — murakkab dizayn muhim bo'lgan hollar uchun (mijozga taqdimot, konferensiya).

---

### Savol 2

**Turi:** scenario

Siz — Artel kompaniyasida loyiha menejeri. Hamkorlik loyihasi yakunlari bo'yicha hamkor uchun taqdimot yaratish kerak. Ma'lumotlar Google Sheets'da, xulosalar Google Docs'da. Cowork uchun qaysi topshiriq eng to'liq bo'ladi?

- A) «Loyiha bo'yicha taqdimot yarat»
- B) «Google Slides'da 8 slaydli taqdimot yarat. Ma'lumotlarni Sheets "Loyiha_Artel_Q1" va xulosalarni Docs "Hisobot_Q1"dan ol. Tuzilma: titul, loyiha maqsadlari, asosiy ko'rsatkichlar, dinamika, natijalar, muammolar, reja, savollar. Har bir slaydga speaker notes. "Taqdimotlar" papkasiga saqlа»
- C) «Loyiha ma'lumotlari asosida animatsiyali chiroyli taqdimot yarat»
- D) «Jadvaldan ma'lumotlarni Google Slides'ga ko'chir, har bir slaydga bitta jadval»

**To'g'ri javob:** B
**Izoh:** B varianti freymvorkning barcha elementlarini o'z ichiga oladi: ma'lumot manbalari (Sheets + Docs), format (aniq tuzilmali 8 slayd), qo'shimcha talablar (speaker notes) va saqlash joyi. C variantida Cowork qo'llab-quvvatlamaydigan animatsiyalar so'ralgan.

---

### Savol 3

**Turi:** multiple_choice

Claude Cowork taqdimotlar yaratishda nimani yaxshi bajaradi? (3 ta to'g'ri javobni tanlang)

- A) Asosiy tezislar bilan slaydlarning mantiqiy tuzilmasi
- B) Gradientlar va animatsiyali murakkab vizual dizayn
- C) Google Sheets'dan ma'lumotli jadvallar
- D) Nutq uchun speaker notes

**To'g'ri javob:** A, C, D
**Izoh:** Claude taqdimot kontenti bilan ajoyib ishlaydi: slaydlarni tuzilmalaydi, qisqa tezislar yaratadi, ma'lumotli jadvallar qo'yadi va speaker notes yozadi. Murakkab dizayn, animatsiyalar va nostandart maketlar — cheklovlar bo'lib, ularni qo'lda yakunlash yaxshiroq.

---

### Savol 4

**Turi:** find_error

Hamkasbingiz mijoz bilan uchrashuv uchun Cowork orqali taqdimot yaratdi. Sizga ko'rsatadi: «Qara, hammasi tayyor — 10 slayd, ma'lumotlar va xulosalar bilan. Ertaga mijozga shunday ko'rsataman». Nimani tekshirish kerak?

- A) Hech narsa — Cowork taqdimot yaratgan, demak hammasi to'g'ri
- B) Vizual bezak: Cowork kontent yaratadi, lekin oddiy dizayn mijoz uchrashuviga mos kelmasligi mumkin — qo'lda yakunlash yoki korporativ shablon qo'llash kerak
- C) Taqdimotni PPTX orqali qayta yaratish kerak, chunki Google Slides sifatsiz
- D) Speaker notes'ni olib tashlash kerak — mijoz ularni ko'rmasligi kerak

**To'g'ri javob:** B
**Izoh:** Claude taqdimot kontentini yaratadi (tuzilma, tezislar, jadvallar), ammo dizayn oddiy bo'ladi. Mijoz uchrashuviga korporativ shablon qo'llash yoki bezakni qo'lda yakunlash kerak. Speaker notes (D) ko'rsatish paytida ko'rinmaydi — bu ma'ruzachi uchun maslahatlar.
