# Hujjatlar va hisobotlar / Dars 2.1: Agentga vazifani qanday qo'yish kerak (prompt emas, topshiriq)

## Metama'lumotlar

| Parametr | Qiymati |
|----------|----------|
| Modul | 2: Hujjatlar va hisobotlar |
| Dars | 2.1 |
| Davomiyligi | 7 daq |
| Turi | Nazariya |

## Video-skript

### Kirish (30 sek)

Assalomu alaykum! O'tgan modulda biz Claude Cowork-ni sozladik va Google Workspace-ni uladik. Endi eng muhim narsani o'rganish vaqti keldi — agentga vazifani qanday to'g'ri qo'yish kerak. Chunki "menga hisobot yoz" bilan "Google Docs-da Google Sheets jadvalidagi ma'lumotlar asosida sotuvlar bo'yicha haftalik hisobot yarat" — bu ikki butunlay boshqa topshiriq. Va natija ham shunga mos bo'ladi.

### Asosiy qism

**Prompt va topshiriq**

Chat-bot bilan ishlaganingizda siz prompt yozasiz — "hisobot yoz" yoki "xat tuz" kabi qisqa so'rov. Chat-bot matn generatsiya qiladi, keyin o'zingiz hal qilasiz: nusxalaysiz, formatlaysiz, hujjatga ko'chirasiz.

Cowork bilan esa boshqacha. Siz topshiriq berasiz — inson-assistentga berganday to'liq ko'rsatma. Va Cowork uni boshidan oxirigacha bajaradi: ma'lumotlarni o'qiydi, hujjat yaratadi, kerakli papkaga saqlaydi.

Farq — "sotuvlar haqida nimadir ayt" bilan "mart oyi bo'yicha sotuvlar hisobotini tayyorla, fevral bilan solishtir, top-3 mahsulotni ajrat va hujjatni Google Drive-dagi 'Hisobotlar' papkasiga joylashtir" o'rtasidagi farqqa o'xshaydi.

**Freymvork: Nima - Qayerdan - Qayerga - Format**

Cowork vazifalarni birinchi marta sifatli bajarishi uchun to'rt elementdan iborat oddiy freymvorkni ishlating:

1. **Nima qilish kerak** — aniq harakat. "Matn yoz" emas, balki "sotuvlar bo'yicha haftalik hisobot yarat"
2. **Ma'lumotlarni qayerdan olish kerak** — axborot manbai. "Google Sheets-dan, 'Sotuvlar mart 2026' jadvali" yoki "biriktirilgan fayldan"
3. **Natijani qayerga joylashtirish kerak** — tayyor hujjat qayerda bo'lishi kerak. "Google Docs-da, 'Hisobotlar/Mart' papkasida"
4. **Qanday formatda** — natija tuzilmasi. "Metrikalar jadvali + 3 ta asosiy xulosa + tavsiyalar"

Keling, misollar ko'raylik.

**1-misol: Haftalik hisobot**

Yomon prompt:
> "Sotuvlar bo'yicha hisobot yoz"

Yaxshi topshiriq:
> "Google Sheets 'Sotuvlar_Q1_2026' dan ma'lumotlarni ol, oxirgi hafta natijalarini tahlil qil. Google Docs-da 'Hisobotlar' papkasida hisobot yarat: asosiy metrikalar jadvali (tushum, bitimlar soni, o'rtacha chek), oldingi hafta bilan foizda solishtirish, va rahbar uchun 3 ta asosiy xulosa"

Farqni ko'ryapsizmi? Ikkinchi holda Cowork nima qilishni, ma'lumotlarni qayerdan olishni, qayerga saqlashni va qanday rasmiylashtirishni aniq biladi.

**2-misol: Ishbilarmonlik xati**

Yomon prompt:
> "Hamkorga xat yoz"

Yaxshi topshiriq:
> "Google Docs-da 'Uzum Market' kompaniyasi uchun ishbilarmonlik xati yarat. Mavzu: xodimlarni o'qitish bo'yicha hamkorlik taklifi. Ohang: professional, lekin samimiy. Tuzilma: salomlashish, taklif mohiyati (3 ta abzats), aniq shartlar, uchrashuvga taklif. Google Drive-dagi 'Xatlar' papkasiga saqlash"

**Cowork rejasini qanday o'qish kerak**

Topshiriq bergandan keyin Cowork darhol bajarishga kirishmaydi. U reja tuzadi va sizga ko'rsatadi. Bu muhim lahza — tasdiqlashdan oldin rejani o'qib chiqing.

Nimaga e'tibor berish kerak:
- **To'g'ri ma'lumot manbai?** Cowork siz ko'rsatgan jadval yoki hujjatga murojaat qilishi kerak
- **Qadamlar ketma-ketligi to'g'rimi?** Avval ma'lumotlarni o'qish, keyin tahlil, keyin hujjat yaratish
- **Saqlash papkasi to'g'rimi?** Hujjat kerakli joyga saqlanishiga ishonch hosil qiling

Agar biror narsa noto'g'ri bo'lsa — tasdiqlashdan oldin ayting. Rejani tuzatish tayyor hujjatni qayta qilishdan osonroq.

**Vazifa qo'yishda tipik xatolar**

Birinchi xato — juda umumiy so'rov. "Bu ma'lumotlar bilan biror narsa qil" — va Cowork sizga aynan nima kerakligini taxmin qilishga majbur bo'ladi.

Ikkinchisi — formatni ko'rsatishni unutish. Siz hisobot olasiz, lekin jadval va tuzilmasiz, uzluksiz matn ko'rinishida, chunki natija qanday ko'rinishi kerakligini aytmagansiz.

Uchinchisi — qayerga saqlashni ko'rsatmaslik. Cowork hujjat yaratishi mumkin, lekin papkani aytmasangiz, uni Google Drive-ning ildiz qismiga joylashtiradi va keyin siz uni qidirib yurasiz.

### Xulosa (30 sek)

Freymvorkni eslab qoling: Nima - Qayerdan - Qayerga - Format. Bu to'rt element noaniq promptni aniq topshiriqqa aylantiradi. Keyingi darsda biz ushbu freymvorkni amalda qo'llaymiz — Google Docs-da to'g'ridan-to'g'ri hisobot, xat va yig'ilish bayonnomasi yaratamiz.

## Matnli qo'llanma

### Prompt va topshiriq: asosiy farq

Chat-bot uchun prompt — bu matn generatsiya qilish so'rovi. Agent uchun topshiriq — bu vazifani boshidan oxirigacha bajarish bo'yicha to'liq ko'rsatma.

| | Prompt (chat-bot) | Topshiriq (Cowork) |
|--|-------------------|-------------------|
| Ifodalanish | "Hisobot yoz" | "Google Sheets ma'lumotlari asosida Google Docs-da hisobot yarat" |
| Natija | Chat oynasidagi matn | Google Docs-dagi tayyor hujjat |
| Sizning ishingiz | Nusxalash, formatlash | Rejani tekshirish va tasdiqlash |
| Ma'lumotlar | O'zingiz qo'lda nusxalaysiz | Cowork o'zi Google Workspace CLI orqali oladi |

### Vazifa qo'yish freymvorki

Cowork uchun har bir topshiriq to'rt elementni o'z ichiga olishi kerak:

**1. Nima qilish kerak** — aniq harakat
- "Sotuvlar bo'yicha haftalik hisobot yarat"
- "Hamkorga ishbilarmonlik xati yoz"
- "Action items bilan yig'ilish bayonnomasi tuz"

**2. Ma'lumotlarni qayerdan olish kerak** — axborot manbai
- "Google Sheets-dan, 'Sotuvlar_Q1' jadvali"
- "Biriktirilgan 'yig'ilish_qaydlari.txt' faylidan"
- "'Loyiha_brifi' Google Doc-dan"

**3. Natijani qayerga joylashtirish kerak** — saqlash joyi
- "Google Docs-da, 'Hisobotlar/Mart' papkasida"
- "Google Drive-da, 'Xatlar' papkasida"
- "Mening Drive-imda yangi Google Doc yarat"

**4. Qanday formatda** — hujjat tuzilmasi
- "Metrikalar jadvali + 3 ta asosiy xulosa"
- "Salomlashish, taklif mohiyati, shartlar, uchrashuvga taklif"
- "Qarorlar (ro'yxat) + vazifalar jadvali (vazifa/mas'ul/muddat) + keyingi qadamlar"

### Topshiriq namunalari

**Haftalik hisobot:**
```
Google Sheets "Sotuvlar_Q1_2026" dan ma'lumotlarni ol.
Oxirgi hafta natijalarini tahlil qil.
Google Docs-da "Hisobotlar" papkasida hisobot yarat:
- Jadval: tushum, bitimlar, o'rtacha chek
- Oldingi hafta bilan solishtirish (%)
- Rahbar uchun 3 ta asosiy xulosa
```

**Ishbilarmonlik xati:**
```
Google Docs-da "Uzum Market" kompaniyasi uchun ishbilarmonlik xati yarat.
Mavzu: xodimlarni o'qitish bo'yicha hamkorlik taklifi.
Ohang: professional, samimiy.
Tuzilma: salomlashish, mohiyat (3 ta abzats), shartlar, uchrashuvga taklif.
Google Drive-dagi "Xatlar" papkasiga saqlash.
```

**Yig'ilish bayonnomasi:**
```
Google Docs-dagi "Qaydlar_rejalashtirish_10mart" hujjatini o'qi.
"Bayonnomalar" papkasida yangi Google Doc-da yig'ilish bayonnomasi yarat:
- Sana va ishtirokchilar
- Qabul qilingan qarorlar (ro'yxat)
- Vazifalar jadvali: vazifa | mas'ul | muddat | holat
- Keyingi qadamlar
```

### Cowork rejasini qanday tekshirish kerak

Bajarishdan oldin Cowork harakatlar rejasini ko'rsatadi. Tekshiring:

| Nimani tekshirish kerak | Nima uchun muhim |
|---------------|-------------|
| Ma'lumot manbai | Cowork to'g'ri jadval/hujjatga murojaat qilishi kerak |
| Qadamlar ketma-ketligi | Avval o'qish, keyin tahlil, keyin yaratish |
| Saqlash papkasi | Hujjat kerakli joyda bo'lishi kerak |
| Natija formati | Tuzilma sizning topshiriqqa mos kelishi kerak |

Agar reja sizni qoniqtirmasa — tasdiqlashdan oldin Cowork-ga ayting. Rejani tuzatish tayyor hujjatni qayta qilishdan osonroq.

## Asosiy xulosalar

1. **Prompt — chat-bot uchun, topshiriq — agent uchun.** Cowork vazifani to'liq bajaradi (ma'lumotlarni o'qishdan hujjatni saqlashgacha), shuning uchun unga qisqa so'rov emas, balki to'liq ko'rsatma kerak
2. **"Nima - Qayerdan - Qayerga - Format" freymvorki** noaniq so'rovni aniq topshiriqqa aylantiradi. Barcha to'rt elementni ko'rsating — va Cowork birinchi marta sifatli natija beradi
3. **Har doim rejani tekshiring** tasdiqlashdan oldin. Cowork to'g'ri manbaga murojaat qilayotganiga, kerakli papkaga saqlayotganiga va to'g'ri formatdan foydalanayotganiga ishonch hosil qiling
