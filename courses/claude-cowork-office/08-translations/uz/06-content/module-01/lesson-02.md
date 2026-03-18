# AI-ofisni sozlash / Dars 1.2: Cowork + Google Workspace CLI o'rnatish va sozlash

## Metama'lumotlar

| Parametr | Qiymati |
|----------|----------|
| Modul | 1: AI-ofisni sozlash |
| Dars | 1.2 |
| Davomiyligi | 10 daq |
| Turi | Amaliyot |

## Video-skript

### Kirish (30 sek)

O'tgan darsda biz agent chat-botdan nimasi bilan farq qilishini tushunib oldik. Endi ishlash uchun zarur bo'lgan hamma narsani sozlaymiz: Claude Desktop'ni o'rnatamiz, Cowork'ni yoqamiz va Google'ning rasmiy vositasi — Google Workspace CLI'ni ulaymiz. Bu dars oxiriga kelib Claude sizning Google Docs va Sheets'ni ko'ra oladigan bo'ladi.

### Asosiy qism

**Sizga nima kerak bo'ladi**

Boshlashdan oldin quyidagilar borligiga ishonch hosil qiling:
- Apple Silicon (M1, M2, M3 yoki yangi) protsessorli Mac
- macOS 14 (Sonoma) yoki yangi versiya
- Claude Pro ($20/oy) yoki Max ($100/oy) obunasi — Cowork bepul rejada mavjud emas
- Google akkaunt (bepul Google Workspace yetarli)

**1-qadam: Claude Desktop o'rnatish (2 daq)**

1. claude.ai/download saytini oching
2. «Download for macOS» tugmasini bosing
3. Yuklab olingan faylni oching
4. Claude.app'ni Applications papkasiga torting
5. Applications'dan Claude Desktop'ni ishga tushiring
6. Pro yoki Max obunali akkauntingiz bilan kiring

Kirganingizdan so'ng oyna yuqorisida uchta varaq ko'rinadi: **Chat**, **Cowork** va **Code**. **Cowork**'ni bosing — bu agent rejimi.

**2-qadam: Google Workspace CLI o'rnatish (3 daq)**

Google Workspace CLI — bu Google'ning rasmiy vositasi (github.com/googleworkspace/cli). U Google Docs, Sheets, Drive, Gmail va Calendar bilan buyruq satri orqali ishlash imkonini beradi. Claude Cowork fayllaringizga kirish uchun undan foydalanadi.

Terminal'ni (Mac'dagi «Terminal» ilovasi) oching va bitta buyruqni bajaring:

```bash
npm install -g @googleworkspace/cli
```

Agar npm o'rnatilmagan bo'lsa, avval nodejs.org saytidan Node.js'ni o'rnating.

O'rnatilganini tekshiring:
```bash
gws --version
```

Agar versiya raqami ko'rinsa — hammasi o'rnatilgan.

**3-qadam: Google akkauntni avtorizatsiya qilish (3 daq)**

Endi Google akkauntingizni ulash kerak. Terminal'da bajaring:

```bash
gws auth setup
```

Bu buyruq hammasini avtomatik qiladi:
- Siz uchun Google Cloud loyihasini yaratadi
- Kerakli API'larni yoqadi (Drive, Docs, Sheets)
- Avtorizatsiya uchun brauzerni ochadi

Brauzerdagi ko'rsatmalarga amal qiling: Google akkauntni tanlang va ruxsat bering. Bu bir martalik jarayon.

Shundan so'ng bajaring:
```bash
gws auth login
```

Kerakli xizmatlarni tanlang (Drive, Docs, Sheets) — va tayyor.

**4-qadam: Ulanishni tekshirish (1 daq)**

`gws` fayllaringizni ko'rayotganini tekshiring:

```bash
gws drive files list --params '{"pageSize": 5}'
```

Agar Google Drive'dagi fayllaringiz ro'yxati ko'rinsa — ulanish ishlayapti.

Endi Claude Desktop → Cowork varag'iga o'ting va yozing:
> «Google Drive'dagi so'nggi fayllarimni gws buyrug'i orqali ko'rsat»

Claude buyruqni bajarib, fayllar ro'yxatini ko'rsatishi kerak.

**Ma'lumotlar xavfsizligi**

Muhim nuqta: Google Workspace CLI orqali Claude sizning Google akkauntingizga kirish huquqini oladi. Quyidagilarni bilish kerak:

- Claude Cowork izolyatsiyalangan muhitda (sandbox) ishlaydi — ma'lumotlar seansdan tashqariga chiqmaydi
- `gws` Google'ning standart OAuth-avtorizatsiyasidan foydalanadi — mobil ilovalar bilan bir xil mexanizm
- Siz `gws`'ning qaysi xizmatlarga kirish huquqi borligini nazorat qilasiz (`gws auth login`da tanlaysiz)
- **Ulash xavfsiz:** ish hujjatlari, hisobotlar, jamlangan ma'lumotli jadvallar
- **Ulash tavsiya etilmaydi:** mijozlarning shaxsiy ma'lumotlari bor hujjatlar (ism + telefon + pasport ma'lumotlari), NDA bilan himoyalangan moliyaviy hisobotlar, parollar va kirish kalitlari

Tavsiya: Google Drive'da Claude bilan ishlash uchun alohida papka yarating va unda faqat AI orqali tahlil qilish xavfsiz bo'lgan fayllarni saqlang.

### Xulosa (30 sek)

Ajoyib! Endi sizda Google Workspace ulangan Claude Cowork sozlangan. E'tibor bering, bu qanchalik oson bo'ldi — Terminal'da ikkita buyruq va Claude allaqachon hujjatlaringizni ko'radi. Keyingi darsda biz CLAUDE.md — Claude'ni oddiy universal AI emas, balki shaxsiy yordamchingizga aylantiradigan fayl yaratamiz.

## Matnli qo'llanma

### Talablar

| Parametr | Talab |
|----------|-------|
| Kompyuter | Apple Silicon (M1/M2/M3+) protsessorli Mac |
| OT | macOS 14 (Sonoma) yoki yangi versiya |
| Obuna | Claude Pro ($20/oy) yoki Max ($100/oy) |
| Google | Bepul Google akkaunt (Workspace shart emas) |
| Node.js | npm orqali gws CLI o'rnatish uchun |

### Bosqichma-bosqich qo'llanma

#### 1. Claude Desktop o'rnatish

1. claude.ai/download saytiga o'ting
2. macOS uchun versiyani yuklab oling
3. Claude.app → Applications'ga torting
4. Ishga tushiring va akkauntga kiring
5. Oyna yuqorisida **Cowork** varag'ini tanlang

#### 2. Google Workspace CLI o'rnatish

Terminal'da:
```bash
# gws CLI o'rnatish
npm install -g @googleworkspace/cli

# O'rnatilganini tekshirish
gws --version
```

Muqobil o'rnatish usullari:
```bash
# Rust orqali (cargo)
cargo install --git https://github.com/googleworkspace/cli --locked

# Nix orqali
nix run github:googleworkspace/cli
```

#### 3. Avtorizatsiya

```bash
# Boshlang'ich sozlash (Google Cloud loyihasini avtomatik yaratadi)
gws auth setup

# Xizmatlarni tanlab avtorizatsiya
gws auth login
```

`gws auth login`da ulashni xohlagan xizmatlarni tanlang:
- Google Drive (fayllar va papkalar)
- Google Docs (hujjatlar)
- Google Sheets (jadvallar)
- Google Calendar (ixtiyoriy)
- Gmail (ixtiyoriy)

#### 4. Tekshirish

```bash
# Drive'ga kirishni tekshirish
gws drive files list --params '{"pageSize": 5}'
```

Keyin Claude Desktop → Cowork'da:
> «Google Drive'dagi fayllarimni gws orqali ko'rsat»

Agar Claude fayllar ro'yxatini ko'rsatsa — sozlash tugallangan.

### Taqqoslash: nima uchun gws, boshqa vositalar emas

| Parametr | Google Workspace CLI (gws) | Uchinchi tomon MCP-serverlar |
|----------|---------------------------|------------------------------|
| Ishlab chiqaruvchi | Google (rasmiy) | Hamjamiyat |
| O'rnatish | 1 buyruq (`npm install`) | Repozitoriyni klonlash, env sozlash |
| OAuth sozlash | Avtomatik (`gws auth setup`) | Qo'lda (Google Cloud Console) |
| Qo'llab-quvvatlanadigan API'lar | Barcha Google Workspace API'lar | Cheklangan to'plam |
| Yangilanishlar | Google'dan | Muallifga bog'liq |

### Ma'lumotlar xavfsizligi

| Xavfsiz | Tavsiya etilmaydi |
|---------|-------------------|
| Ish hisobotlari | Mijozlarning shaxsiy ma'lumotlari |
| Jamlangan jadvallar | NDA bilan himoyalangan moliyaviy hisobotlar |
| Hujjat shablonlari | Parollar va kirish kalitlari |
| Xatlarning qoralama nusxalari | Tibbiy ma'lumotli hujjatlar |

**Tavsiya:** Google Drive'da Claude bilan ishlash uchun alohida papka yarating.

### Muammolarni bartaraf etish

| Muammo | Yechim |
|--------|--------|
| `npm: command not found` | nodejs.org saytidan Node.js'ni o'rnating |
| `gws: command not found` | O'rnatishdan so'ng Terminal'ni qayta ishga tushiring |
| Avtorizatsiya xatosi | `gws auth login`ni qaytadan bajaring |
| Claude fayllarni ko'rmayapti | Terminal'da `gws drive files list`ni tekshiring |
| Docs/Sheets'ga kirish yo'q | `gws auth login`da kerakli xizmatlarni tanlang |

## Asosiy xulosalar

1. **Cowork uchun Mac** (Apple Silicon, macOS 14+) va **Pro yoki Max obuna** kerak. Bepul rejada agent rejimi mavjud emas
2. **Google Workspace CLI** — Google'ning rasmiy vositasi. O'rnatish: `npm install -g @googleworkspace/cli`, avtorizatsiya: `gws auth setup` → `gws auth login`. Uchinchi tomon MCP-serverlarni sozlashdan osonroq
3. **Xavfsizlik:** Claude sandbox'da ishlaydi, `gws` esa Google'ning standart OAuth-avtorizatsiyasidan foydalanadi. AI bilan ishlash uchun alohida papka yarating va shaxsiy ma'lumotli hujjatlarni ulamang
