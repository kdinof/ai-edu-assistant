# Avtomatlashtirish va natija / Dars 5.1: Skills: takrorlanuvchi vazifalar uchun shablonlar

## Metama'lumotlar

| Parametr | Qiymat |
|----------|--------|
| Modul | 5: Avtomatlashtirish va natija |
| Dars | 5.1 |
| Davomiyligi | 7 min |
| Turi | Nazariya |

## Video-skript

### Kirish (30 sek)

Assalomu alaykum! Oldingi modullarda siz hujjatlar yaratishni, jadvallar bilan ishlashni va pipeline'lar yig'ishni o'rgandingiz. Lekin har safar topshiriqni qaytadan yozardingiz. Agar har hafta bajariladigan vazifangiz bo'lsa — nima uchun topshiriqni har safar qayta tuzasiz? Ushbu darsda skills — muvaffaqiyatli topshiriqni saqlash va uni bitta buyruq bilan ishga tushirish usulini ko'rib chiqamiz.

### Asosiy qism

**Skill nima?**

Skill — bu siz muntazam bajaradigan vazifa uchun saqlangan ko'rsatma. Har safar «Jadvaldan ma'lumot ol, tahlil qil, hisobot yarat...» deb yozish o'rniga, siz bu topshiriqni bir marta saqlaysiz va keyin bitta ibora bilan ishga tushirasiz.

Qiyoslash: skill — bu retseptga o'xshaydi. Siz ingrediyentlar va bosqichlarni bir marta yozib qo'yasiz, keyin har safar proportiyalarni eslamasdan, shu retsept bo'yicha tayyorlaysiz.

**Skill'larni qayerdan olish mumkin?**

Eng yaxshi skill'lar — bu allaqachon yaxshi natija bergan topshiriqlar. 2-4-modullarda siz hujjatlar yaratdingiz, jadvallarni tahlil qildingiz, pipeline'lar yig'dingiz. Topshiriqlaringizga qarang:

- Qaysi vazifalarni har hafta bajarasiz?
- Qaysi topshiriq birinchi urinishdayoq yaxshi natija berdi?
- Qaysi topshiriqni nusxalab, qayta ishlatgan bo'lardingiz?

Mana shu — skill'larga nomzodlar.

**Skill qanday yaratiladi?**

Cowork'dagi skill — bu ko'rsatma yozilgan alohida fayl. Uni ikki usulda yaratish mumkin:

**1-usul — Cowork interfeysi orqali:**
1. Claude Desktop → Settings → Capabilities → Skills ni oching
2. «Add Skill» tugmasini bosing
3. Nom bering va ko'rsatma matnini kiriting
4. Saqlang

**2-usul — Cowork'dan so'rang:**
> «"Juma hisoboti" nomli skill yarat, ko'rsatmasi:
> 1. Google Sheets "Vazifalar_jamoa" ni och
> 2. Statusni yig': bajarildi, jarayonda, muddati o'tgan
> 3. Google Docs da "Hisobotlar/Haftalik" papkasida hisobot yarat: statuslar jadvali, muammoli vazifalar, 3 ta asosiy xulosa»

Cowork skill faylini yaratadi va avtomatik saqlaydi.

Yaratilgandan so'ng, skill bitta ibora bilan ishga tushiriladi:
> «Juma hisoboti»

Cowork vazifani skill tavsifi bo'yicha taniydi va ko'rsatmani bajaradi.

**Namoyish: «Juma hisoboti» skill'i**

Skill'siz: har juma topshiriqni tuzishga 3-5 minut sarflaysiz. Ba'zan papkani yoki formatni ko'rsatishni unutasiz. Natija har safar biroz farq qiladi.

Skill bilan: bitta ibora — va Cowork saqlangan ko'rsatma bo'yicha bajaradi. Natija har hafta barqaror.

**Ofis vazifalari uchun skill'lar namunalari**

| Skill | Nima qiladi | Chastotasi |
|-------|------------|-----------|
| Juma hisoboti | Vazifalar statusi → Docs da hisobot | Haftada 1 marta |
| Rejalashtiruvga tayyorgarlik | Sheets dan ma'lumotlar → kun tartibi + bayonnoma shabloni | Haftada 1 marta |
| Uchrashuv bayonnomasi | Eslatmalar → action items bilan bayonnoma Docs da | Haftada 2-3 marta |
| Xarajatlar tahlili | Xarajatlar jadvali → xulosa + tahlil | Oyda 1 marta |
| Rasmiy xat | Mavzu + manzil → kerakli formatda xat | So'rov bo'yicha |

**Yaxshi skill'lar qoidalari**

1. **Aniqlik.** Skill 4 ta elementni o'z ichiga olishi kerak: Nima → Qayerdan → Qayerga → Format. Bularsiz natija har safar farq qiladi
2. **Muntazamlik.** Kamida haftada bir marta bajariladigan vazifalar uchun skill yarating. Bir martalik vazifalar uchun skill — ortiqcha ish
3. **Tekshirilganlik.** Skill = allaqachon yaxshi natija bergan topshiriq. Hech qachon sinab ko'rmagan topshiriqni skill sifatida saqlamang

**Antipattern: hamma narsa uchun skill**

Har bir harakat uchun skill yaratish shart emas. «Xatga javob yoz» uchun skill — ortiqcha, chunki har bir xat noyobdir. Skill foydali bo'ladi, qachonki vazifa tuzilishi takrorlanib, faqat ma'lumotlar o'zgarsa.

### Xulosa (30 sek)

Skill — bitta buyruq bilan ishlaydigan saqlangan topshiriq. 2-4-modullardan yaxshi natija bergan vazifani oling va Cowork orqali undan skill yarating. Keyingi darsda bir necha bosqichli skill'lar yaratishni — butun ish jarayonini avtomatlashtiradigan zanjirlarni ko'rib chiqamiz.

## Matnli qo'llanma

### Skill nima?

Skill — muntazam vazifa uchun saqlangan ko'rsatma. Cowork'da alohida fayl sifatida saqlanadi va bitta ibora bilan ishga tushiriladi.

**Skill'siz:** har safar topshiriqni qaytadan yozasiz (3-5 min), ba'zan tafsilotlarni unutasiz, natija beqaror.
**Skill bilan:** bitta ibora → har safar barqaror natija.

### Skill qanday yaratiladi

**Interfeys orqali:**
1. Claude Desktop → Settings → Capabilities → Skills → Add Skill
2. Nom va ko'rsatmani kiriting
3. Saqlang

**Cowork orqali:**
> «"[nom]" nomli skill yarat, ko'rsatmasi: [topshiriq matni]»

**Ishga tushirish:**
> «[Skill nomi]» — Cowork vazifani taniydi va ko'rsatma bo'yicha bajaradi

### Skill namunasi: Juma hisoboti

**Nomi:** Juma hisoboti

**Ko'rsatma:**
```
Har juma:
1. Google Sheets "Vazifalar_jamoa" ni och
2. Statusni yig': bajarildi, jarayonda, muddati o'tgan
3. Google Docs da "Hisobotlar/Haftalik" papkasida hisobot yarat:
   - Statuslar jadvali
   - Muammoli vazifalar
   - 3 ta asosiy xulosa
4. Format: jadval + xulosalar, ortiqcha so'zsiz
```

### Skill namunasi: Rejalashtiruvga tayyorgarlik

**Nomi:** Rejalashtiruvga tayyorgarlik

**Ko'rsatma:**
```
Har dushanba ertalab:
1. Google Sheets "Vazifalar_jamoa" ni och — haftalik status
2. Google Docs da "Rejalashtiruvlar" papkasida kun tartibini yarat:
   - Vazifalar statusi (jadval)
   - Muammoli vazifalar (ro'yxat)
   - Muhokama uchun savollar
3. Har bir bandga — tezislar (2-3 gap)
4. Hujjat oxirida bayonnoma shabloni
```

### Yaxshi skill'lar qoidalari

| Qoida | Sababi |
|-------|--------|
| Aniqlik | 4 ta elementsiz (Nima/Qayerdan/Qayerga/Format) natija beqaror |
| Muntazamlik | Yilda bir marta bajariladigan vazifa uchun skill — ortiqcha ish |
| Tekshirilganlik | Faqat allaqachon yaxshi natija bergan topshiriqlarni saqlang |

## Asosiy xulosalar

1. **Skill** — muntazam vazifa uchun saqlangan ko'rsatma. Settings → Skills → Add Skill orqali yoki Cowork orqali bitta buyruq bilan yaratiladi. Skill nomi bilan ishga tushiriladi
2. **Eng yaxshi skill'lar** — bu 2-4-modullarda allaqachon yaxshi natija bergan topshiriqlar. Yangi narsalarni o'ylab topmang — ishlaganni oling va skill sifatida saqlang
3. **Skill muntazam vazifalar uchun foydali** — takrorlanuvchi tuzilishga ega bo'lganlar (hisobotlar, uchrashuvlarga tayyorgarlik, bayonnomalar). Noyob bir martalik vazifalar uchun skill yaratish shart emas
