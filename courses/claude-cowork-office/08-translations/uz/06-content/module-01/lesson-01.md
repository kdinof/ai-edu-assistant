# AI-ofisni sozlash / Dars 1.1: Chat-bot va agent: nima uchun Cowork — bu boshqacha yondashuv

## Metama'lumotlar

| Parametr | Qiymati |
|----------|----------|
| Modul | 1: AI-ofisni sozlash |
| Dars | 1.1 |
| Davomiyligi | 5 daq |
| Turi | Nazariya |

## Video-skript

### Kirish (30 sek)

Assalomu alaykum! Agar siz hech bo'lmaganda bir marta ChatGPT yoki Claude'dan ish uchun foydalangan bo'lsangiz, bu jarayonni bilasiz: so'rov yozdingiz, matn oldingiz, hujjatga nusxaladingiz, formatlash qildingiz, tuzatdingiz. Va har safar shunday.

Bu darsda men Claude Cowork nima uchun tubdan boshqacha ishlashini va bu nima uchun kundalik vazifalarga yondashuvni o'zgartirishini ko'rsataman.

### Asosiy qism

**Ishda AI'ga ikki xil yondashuv**

Bir vazifani tasavvur qiling: rahbar uchun haftalik sotuv hisobotini tayyorlash kerak.

**1-yondashuv — chat-bot (ChatGPT, oddiy Claude):**
1. ChatGPT'ni ochasiz
2. Jadvaldan ma'lumotlarni chatga nusxalaysiz
3. Yozasiz: «Bu ma'lumotlar bo'yicha hisobot qil»
4. Matn olasiz
5. Google Docs'ga nusxalaysiz
6. Formatlash qilasiz
7. Jadvalni qo'lda qo'shasiz
8. Hech narsa yo'qolmaganini tekshirasiz

Jami: 8 qadam, 20-30 daqiqa qo'l mehnati. Va har hafta shunday.

**2-yondashuv — agent (Claude Cowork + Google Workspace CLI):**
1. Topshiriq yozasiz: «Google Sheets'dagi "Q1 Sotuvlar" jadvalidan ma'lumotlarni ol, asosiy ko'rsatkichlar va xulosalar bilan haftalik hisobot yarat, Google Docs'da "Hisobotlar" papkasiga saqla»
2. Cowork rejani ko'rsatadi: nima qilmoqchi ekanini
3. Siz tasdiqlaysiz
4. Cowork bajaradi: jadvalni ochadi, ma'lumotlarni tahlil qiladi, formatlangan hujjat yaratadi, kerakli papkaga saqlaydi

Jami: 1 ta topshiriq, 2 daqiqa sizning vaqtingiz. Natija — Google Docs'da tayyor hujjat.

**Buni nima imkoniyatga aylantiradi: Google Workspace CLI**

Google Workspace CLI (`gws`) — bu Google'ning rasmiy vositasi bo'lib, u Google Docs, Sheets, Drive, Gmail va Calendar bilan buyruq satri orqali ishlash imkonini beradi. Claude Cowork `gws`'ga ulanganda, u sizning Google Workspace'dagi fayllarni bevosita o'qiy va yarata oladi.

`gws`'siz: Claude — matn yaratadigan suhbatdosh. `gws` bilan — fayllaringiz bilan bevosita ishlaydigan yordamchi.

O'xshatish: chat-bot — bu sizga telefon orqali aytib turgan, u esa qog'ozga yozib olayotgan hamkasb. Google Workspace CLI bilan agent esa — kompyuteringiz oldida o'tirib, vazifani o'zi bajarayotgan yordamchi.

**Asosiy xato**

Eng keng tarqalgan xato — Cowork'dan chat-bot sifatida foydalanish. «Menga hisobot yoz» deb yozish va natijani nusxalash. Bu xuddi yordamchi yollab, undan faqat matn aytib berishni so'rashga o'xshaydi.

To'g'ri yondashuv: vazifani to'liq qo'yish. «Hisobot matnini yoz» emas, balki «Google Sheets'dagi ma'lumotlar asosida Google Docs'da hisobot yarat». Cowork hammasini o'zi qiladi — ma'lumotlarni tahlil qilishdan tortib tayyor hujjatni saqlashgacha.

### Xulosa (30 sek)

Xulosa qilib aytganda, asosiy farq shundaki: chat-bot matn yaratadi, keyin siz uni qo'lda ish vositalariga ko'chirasiz. Agent esa vazifani to'liq bajaradi — ma'lumotlardan Google Workspace'dagi tayyor hujjatgacha.

Keyingi darsda biz Claude Desktop'ni o'rnatamiz, Google Workspace CLI'ni ulaymiz va hamma narsa ishlayotganini tekshiramiz.

## Matnli qo'llanma

### Chat-bot va agent: farqi nimada

Ko'pchilik AI'dan chat-bot sifatida foydalanadi: so'rov yozadi, matn oladi, hujjatga nusxalaydi. Bu yordam beradi, lekin ko'p qo'l mehnati yaratadi: nusxalash, formatlash, tekshirish.

Claude Cowork boshqacha ishlaydi. Bu **agent rejimi**: siz vazifa qo'yasiz, Cowork reja tuzadi, siz tasdiqlaysiz va u ishni bevosita sizning ish vositalaringizda bajaradi.

### Amalda qanday ishlaydi

| Bosqich | Chat-bot | Agent (Cowork) |
|---------|----------|----------------|
| Ma'lumot kiritish | Siz ma'lumotlarni chatga nusxalaysiz | Cowork o'zi Google Sheets'dan ma'lumotlarni o'qiydi |
| Qayta ishlash | Matn yaratadi | Tahlil qiladi, formatlangan hujjat yaratadi |
| Natija | Chat oynasidagi matn | Google Docs'dagi tayyor hujjat |
| Sizning ishingiz | Nusxalash, formatlash | Rejani tasdiqlash |

### Google Workspace CLI — Claude va Google o'rtasidagi ko'prik

Google Workspace CLI (`gws`) — Google'ning Docs, Sheets, Drive, Gmail va Calendar bilan buyruq satridan ishlash uchun rasmiy vositasi. Claude Cowork `gws` orqali fayllaringizga kiradi.

`gws`'siz: Claude faqat matn yarata oladi.
`gws` bilan: Claude jadvallaringizni o'qiydi, hujjatlar yaratadi, fayllarni saqlaydi — barchasi sizning ishtirokisiz.

### «Agentga vazifa qo'yish» nimani anglatadi

«Menga hisobot matnini yoz» emas, balki:
- **Nima qilish kerak:** haftalik hisobot yaratish
- **Ma'lumotni qayerdan olish:** Google Sheets, «Q1 Sotuvlar» jadvali
- **Natijani qayerga joylashtirish:** Google Docs, «Hisobotlar» papkasi
- **Qanday formatda:** ko'rsatkichlar jadvali + 3 ta asosiy xulosa

Bu freymvork — **Nima - Qayerdan - Qayerga - Format** — butun kurs davomida foydalanamiz.

## Asosiy xulosalar

1. **Chat-bot matn yaratadi**, keyin siz uni qo'lda hujjatlarga ko'chirasiz. **Agent vazifani to'liq bajaradi** — ma'lumotlardan Google Workspace'dagi tayyor natijagacha
2. **Google Workspace CLI** (`gws`) — Google'ning rasmiy vositasi bo'lib, Claude'ga Docs, Sheets, Drive bilan bevosita ishlash imkonini beradi. Usiz Cowork fayllaringiz bilan ishlay olmaydi
3. **Asosiy xato** — Cowork'dan oddiy chat-bot sifatida matn yaratish uchun foydalanish. To'g'ri yondashuv: vazifani «Nima - Qayerdan - Qayerga - Format» freymvorki bo'yicha to'liq qo'yish
