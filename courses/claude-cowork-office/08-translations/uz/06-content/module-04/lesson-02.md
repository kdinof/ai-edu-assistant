# Taqdimotlar va payplaynlar / Dars 4.2: Payplayn: ma'lumotlar → hisobot → taqdimot

## Metama'lumotlar

| Parametr | Qiymati |
|----------|----------|
| Modul | 4: Taqdimotlar va payplaynlar |
| Dars | 4.2 |
| Davomiyligi | 8 daq |
| Turi | Nazariya |

## Video-skript

### Kirish (30 sek)

Assalomu alaykum! Hozirgacha biz Cowork'ni alohida vazifalar uchun ishlatdik: hujjat yaratish, jadvalni tahlil qilish, taqdimot tayyorlash. Ammo agentning haqiqiy kuchi — vazifalar zanjiridadir, bunda bir qadamning natijasi keyingisi uchun kiruvchi ma'lumot bo'ladi. Bu payplayn deb ataladi.

### Asosiy qism

**Payplayn nima**

Payplayn — vazifalar zanjiri bo'lib, har bir qadam avvalgisiga asoslanadi:

1. **Ma'lumotlar** (Google Sheets) → 2. **Tahlil** (xulosalar bilan yangi varaq) → 3. **Hisobot** (Google Docs) → 4. **Taqdimot** (Google Slides)

Cowork'siz siz har bir qadamni qo'lda bajarasiz: jadvalni ochasiz, raqamlarni hujjatga nusxalaysiz, formatlaysiz, keyin tezislarni taqdimotga ko'chirasiz. Bu 4 ta vosita va 30-60 daqiqa ish.

Cowork bilan — bitta topshiriq. U butun zanjirni Google Workspace CLI orqali bajaradi: ma'lumotlarni o'qiydi, tahlil qiladi, hujjat yaratadi, taqdimot shakllantiradi. Natija — 4 ta bog'langan artefakt.

**Namoyish: to'liq tsikl**

Faraz qilaylik, vazifa shunday: rahbariyat uchun choraklik hisobot tayyorlash. Google Sheets'da savdo jadvali bor.

Cowork uchun topshiriq shunday ko'rinadi:

> «Q1 2026 yakunlari bo'yicha hujjatlar to'plamini tayyorla:
> 1. Google Sheets "Savdo_Q1_2026"ni och. Ma'lumotlarni tahlil qil: umumiy tushum, oylar bo'yicha dinamika, top-5 mahsulot, Q4 2025 bilan solishtirish. "Tahlil Q1" varaqiga natijalarni yoz.
> 2. Tahlil asosida Google Docs'da "Hisobotlar" papkasiga hisobot yarat: asosiy ko'rsatkichlar (jadval), 3 ta asosiy xulosa, Q2 uchun tavsiyalar.
> 3. Hisobotdan Google Slides'da 7 slaydli taqdimot yarat, "Taqdimotlar" papkasiga: titul, ko'rsatkichlar, dinamika, top-mahsulotlar, xulosalar, Q2 reja, savollar. Har bir slaydga — speaker notes.»

Bitta topshiriq — uchta artefakt:
- Google Sheets'da «Tahlil Q1» varag'i
- Google Docs'da hisobot
- Google Slides'da taqdimot

Hammasi bog'langan: taqdimotdagi raqamlar hisobot bilan mos keladi, chunki bitta manbadan olingan.

**Bitta topshiriq va bosqichma-bosqich buyruqlar**

Muhim qoida: butun payplaynni bitta topshiriqda tasvirlang, buyruqlarni birma-bir bermang.

| Yondashuv | Namuna | Natija |
|--------|--------|-----------|
| Birma-bir buyruq | «Avval jadvalni tahlil qil» → kutasiz → «Endi hisobot yarat» → kutasiz → «Endi taqdimot» | 3 ta iteratsiya, har bir qadamni kutish va tekshirish kerak |
| Bitta payplayn | «Jadvalni tahlil qil → hisobot yarat → taqdimot tayyorla» | Cowork butun zanjirni bajaradi, siz rejani bir marta tekshirasiz |

Butun zanjirni birdaniga tasvirlaganingizda, Cowork yakuniy maqsadni ko'radi va oraliq qadamlarni yaxshiroq rejalashtiradi. U biladi — tahlil ma'lumotlari hisobotga, hisobotdagi tezislar esa taqdimotga boradi.

**Payplayn rejasini qanday o'qish kerak**

Bajarishdan oldin Cowork reja ko'rsatadi — qadamlar ketma-ketligini. Payplayn uchun tekshiring:

1. **To'g'ri tartib:** avval ma'lumotlar, keyin tahlil, keyin hujjatlar
2. **Qadamlar orasidagi bog'lanishlar:** 1-qadamdagi ma'lumotlar 2-qadamda ishlatiladi, qayta o'qilmaydi
3. **To'g'ri papkalar:** har bir artefakt ko'rsatilgan joyga saqlanadi
4. **Barcha qadamlar mavjud:** 3 ta artefakt so'ragan bo'lsangiz — rejada 3 ta qadam bo'lishi kerak

Biror narsa noto'g'ri bo'lsa — tasdiqlashdan oldin to'g'rilang.

**Payplayn qachon ortiqcha**

Payplayn foydali:
- Aniq zanjir mavjud: ma'lumotlar → tahlil → hujjat → taqdimot
- Artefaktlar umumiy ma'lumot manbasi bilan bog'langan
- Vazifa muntazam takrorlanadi (har hafta, har oy)

Payplayn ortiqcha:
- Vazifa bir martalik va oddiy (bitta xat, bitta hisobot)
- Qadamlar bir-biridan mustaqil (umumiy ma'lumotlar ishlatilmaydi)
- Keyingi qadamdan oldin har bir oraliq natijani tekshirish kerak

### Xulosa (30 sek)

Payplayn — bu Cowork siz uchun vazifalar zanjirini bajaradigan jarayon: jadvaldagi ma'lumotlardan tayyor taqdimotgacha. Asosiy qoida: butun tsiklni bitta topshiriqda tasvirlang, bosqichma-bosqich emas. Keyingi darsda payplaynni aniq vazifaga tatbiq etamiz — ish uchrashuviga tayyorgarlik.

## Matnli qo'llanma

### Payplayn nima

Payplayn — vazifalar zanjiri bo'lib, har bir qadamning natijasi → keyingisi uchun kiruvchi ma'lumot:

```
Google Sheets (ma'lumotlar) → Tahlil (yangi varaq) → Google Docs (hisobot) → Google Slides (taqdimot)
```

**Cowork'siz:** 4 ta vosita, ular orasida qo'lda nusxalash, 30-60 daqiqa.
**Cowork bilan:** 1 ta topshiriq, gws orqali avtomatik zanjir, sizning vaqtingizdan 3-5 daqiqa.

### Payplayn uchun topshiriq shabloni

```
[mavzu] bo'yicha hujjatlar to'plamini tayyorla:

1. Google Sheets "[nomi]"ni och.
   Tahlil qil: [aniq savollar].
   Natija — "[varaq nomi]" varag'ida.

2. Tahlil asosida Google Docs'da
   "[papka]" papkasiga hisobot yarat:
   [hisobot tuzilmasi tavsifi].

3. Hisobotdan Google Slides'da
   [N] slaydli taqdimot yarat, "[papka]" papkasiga:
   [slaydlar tuzilmasi].
   Har bir slaydga — speaker notes.
```

### Bitta topshiriq va bosqichma-bosqich buyruqlar

| | Bosqichma-bosqich | Payplayn |
|--|----------|----------|
| Ifodalash | 3 ta alohida so'rov | 1 ta kompleks topshiriq |
| Sizning ishtirokingiz | Har bir qadamni tekshirasiz | Rejani bir marta tekshirasiz |
| Bog'lanish | Qadamlarni o'zingiz bog'laysiz | Cowork butun zanjirni ko'radi |
| Vaqt | 15-20 daq (kutish bilan) | 3-5 daq |

### Payplayn rejasi cheklisti

Rejani tasdiqlashdan oldin tekshiring:
- [ ] Qadamlar tartibi to'g'ri (ma'lumotlar → tahlil → hujjat → taqdimot)
- [ ] 1-qadamdagi ma'lumotlar 2-qadamda ishlatiladi (qayta o'qilmaydi)
- [ ] Har bir artefakt ko'rsatilgan papkaga saqlanadi
- [ ] Barcha so'ralgan qadamlar rejada mavjud

## Asosiy xulosalar

1. **Payplayn** — vazifalar zanjiri bo'lib, Cowork har bir qadamning natijasini keyingisiga avtomatik uzatadi: ma'lumotlar → tahlil → hisobot → taqdimot. Vositalar orasida qo'lda nusxalash o'rniga — bitta topshiriq
2. **Butun payplaynni bitta topshiriqda tasvirlang**, bosqichma-bosqich emas. Cowork yakuniy maqsadni ko'radi va oraliq qadamlarni yaxshiroq rejalashtiradi. Siz rejani uch marta emas, bir marta tekshirasiz
3. **Payplayn muntazam vazifalar uchun foydali** — aniq zanjir va umumiy ma'lumot manbasi mavjud bo'lganda. Bir martalik oddiy vazifalar uchun — zanjirsiz bitta topshiriq yetarli
