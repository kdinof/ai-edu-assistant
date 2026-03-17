# AI-ofisni sozlash / Dars 1.1: Chat-bot va agent: nima uchun Cowork — boshqacha yondashuv

## Metama'lumotlar

| Parametr | Qiymat |
|----------|--------|
| Modul | 1: AI-ofisni sozlash |
| Dars | 1.1 |
| Davomiyligi | 5 daq |
| Turi | Nazariya |

## Video-skript

### Kirish (30 sek)

Assalomu alaykum! Agar siz hech bo'lmaganda bir marta ChatGPT yoki Claude'dan ish uchun foydalangan bo'lsangiz, bu jarayonni bilasiz: so'rov yozdingiz, matn oldingiz, hujjatga ko'chirdingiz, formatlashtirib chiqdingiz. Va har safar shunday.

Bu darsda men sizga Claude Cowork nima uchun tubdan boshqacha ishlashini va bu kundalik vazifalariga yondashuvni qanday o'zgartirishini ko'rsataman.

### Asosiy qism

**Ishda AI'ga ikki yondashuv**

Tasavvur qiling: rahbar uchun haftalik sotuv hisobotini tayyorlash kerak.

**1-yondashuv — chat-bot (ChatGPT, oddiy Claude):**
1. ChatGPT'ni ochasiz
2. Jadvaldan ma'lumotlarni chatga ko'chirasiz
3. Yozasiz: "Bu ma'lumotlar asosida hisobot yoz"
4. Matn olasiz
5. Google Docs'ga ko'chirasiz
6. Formatlaysiz
7. Jadvalni qo'lda qo'shasiz
8. Hech narsa yo'qolmaganini tekshirasiz

Jami: 8 qadam, 20-30 daqiqa qo'l mehnati. Va har hafta shunday.

**2-yondashuv — agent (Claude Cowork + Google Workspace CLI):**
1. Vazifa yozasiz: "Google Sheets'dagi 'Sotuvlar Q1' jadvalidan ma'lumotlarni ol, asosiy ko'rsatkichlar va xulosalar bilan haftalik hisobot tuzib, Google Docs'da 'Hisobotlar' papkasiga saqlа"
2. Cowork rejani ko'rsatadi: nima qilmoqchi ekanini
3. Siz tasdiqlaysiz
4. Cowork bajaradi: jadvalni ochadi, ma'lumotlarni tahlil qiladi, formatlangan hujjat yaratadi, kerakli papkaga saqlaydi

Jami: 1 ta vazifa, 2 daqiqa sizning vaqtingiz. Natija — Google Docs'da tayyor hujjat.

**Buni nima imkon qiladi: Google Workspace CLI**

Google Workspace CLI (`gws`) — bu Google'ning rasmiy vositasi bo'lib, Google Docs, Sheets, Drive, Gmail va Calendar bilan buyruq satri orqali ishlash imkonini beradi. Claude Cowork `gws`ga ulanganda, u sizning Google Workspace'dagi fayllaringizni to'g'ridan-to'g'ri o'qiy oladi va yarata oladi.

`gws`siz: Claude — matn yaratuvchi suhbatdosh. `gws` bilan — fayllaringiz bilan bevosita ishlaydigan yordamchi.

O'xshatma: chat-bot — bu siz telefon orqali diktovka qilasiz, u esa qog'ozga yozib oladi. Google Workspace CLI'li agent — bu sizning kompyuteringiz oldida o'tirib, vazifani o'zi bajaradigan yordamchi.

**Asosiy xato**

Eng ko'p tarqalgan xato — Cowork'dan chat-bot sifatida foydalanish. "Menga hisobot yoz" deb yozib, natijani ko'chirib olish. Bu — yordamchi yollab, undan faqat matn diktovka qilishni so'rash bilan barobar.

To'g'ri yondashuv: vazifani to'liq qo'yish. "Hisobot matni yoz" emas, balki "Google Sheets'dagi ma'lumotlar asosida Google Docs'da hisobot yarat". Cowork hammasini o'zi qiladi — ma'lumotlarni tahlil qilishdan tayyor hujjatni saqlashgacha.

### Xulosa (30 sek)

Xullas, asosiy farq shundaki: chat-bot matn yaratadi, keyin siz uni qo'lda ish vositalariga ko'chirasiz. Agent esa vazifani to'liq bajaradi — ma'lumotlardan Google Workspace'dagi tayyor hujjatgacha.

Keyingi darsda biz Claude Desktop'ni o'rnatamiz, Google Workspace CLI'ni ulaymiz va hammasining ishlayotganini tekshiramiz.

## Matnli qo'llanma

### Chat-bot va agent: farqi nimada

Ko'pchilik AI'dan chat-bot sifatida foydalanadi: so'rov yozadi, matn oladi, hujjatga ko'chiradi. Bu foydali, lekin ko'p qo'l mehnati talab qiladi: nusxalash, formatlash, tekshirish.

Claude Cowork boshqacha ishlaydi. Bu **agent rejimi**: siz vazifa qo'yasiz, Cowork reja tuzadi, siz tasdiqlaysiz va u ishni to'g'ridan-to'g'ri sizning ish vositalaringizda bajaradi.

### Amalda bu qanday ishlaydi

| Bosqich | Chat-bot | Agent (Cowork) |
|---------|----------|----------------|
| Ma'lumot kiritish | Siz ma'lumotlarni chatga ko'chirasiz | Cowork o'zi Google Sheets'dan o'qiydi |
| Qayta ishlash | Matn yaratadi | Tahlil qiladi, formatlangan hujjat yaratadi |
| Natija | Chat oynasidagi matn | Google Docs'dagi tayyor hujjat |
| Sizning ishingiz | Nusxalash, formatlash | Rejani tasdiqlash |

### Google Workspace CLI — Claude va Google o'rtasidagi ko'prik

Google Workspace CLI (`gws`) — Docs, Sheets, Drive, Gmail va Calendar bilan buyruq satridan ishlash uchun Google'ning rasmiy vositasi. Claude Cowork fayllaringizga kirish uchun `gws`dan foydalanadi.

`gws`siz: Claude faqat matn yarata oladi.
`gws` bilan: Claude jadvallaringizni o'qiydi, hujjatlar yaratadi, fayllarni saqlaydi — barchasi sizning ishtirokingiz holda.

### "Agentga vazifa qo'yish" nimani anglatadi

"Menga hisobot matni yoz" emas, balki:
- **Nima qilish kerak:** haftalik hisobot yaratish
- **Ma'lumotni qayerdan olish:** Google Sheets, "Sotuvlar Q1" jadvali
- **Natijani qayerga qo'yish:** Google Docs, "Hisobotlar" papkasi
- **Qanday formatda:** ko'rsatkichlar jadvali + 3 ta asosiy xulosa

Bu freymvork — **Nima - Qayerdan - Qayerga - Format** — butun kurs davomida ishlatiladi.

## Asosiy xulosalar

1. **Chat-bot matn yaratadi**, keyin siz uni qo'lda hujjatlarga ko'chirasiz. **Agent vazifani to'liq bajaradi** — ma'lumotlardan Google Workspace'dagi tayyor natijagacha
2. **Google Workspace CLI** (`gws`) — Google'ning rasmiy vositasi bo'lib, Claude'ga Docs, Sheets, Drive bilan bevosita ishlash imkonini beradi. Usiz Cowork fayllaringiz bilan ishlay olmaydi
3. **Asosiy xato** — Cowork'dan oddiy chat-bot sifatida matn yaratish uchun foydalanish. To'g'ri yondashuv: vazifani "Nima - Qayerdan - Qayerga - Format" freymvorki bo'yicha to'liq qo'yish
