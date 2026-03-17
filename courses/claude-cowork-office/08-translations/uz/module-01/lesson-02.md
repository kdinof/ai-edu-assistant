# AI-ofisni sozlash / Dars 1.2: Cowork + Google Workspace CLI o'rnatish va sozlash

## Metama'lumotlar

| Parametr | Qiymat |
|----------|--------|
| Modul | 1: AI-ofisni sozlash |
| Dars | 1.2 |
| Davomiyligi | 10 daq |
| Turi | Amaliyot |

## Video-skript

### Kirish (30 sek)

O'tgan darsda biz agentning chat-botdan farqini tushundik. Endi ishlash uchun zarur hamma narsani sozlaymiz: Claude Desktop'ni o'rnatamiz, Cowork'ni yoqamiz va Google Workspace CLI — Google'ning rasmiy vositasini ulaymiz. Ushbu dars oxirida Claude sizning Google Docs va Sheets'laringizni ko'ra oladi.

### Asosiy qism

**Sizga nima kerak**

Boshlashdan oldin quyidagilar borligiga ishonch hosil qiling:
- Apple Silicon (M1, M2, M3 yoki yangi) protsessorli Mac
- macOS 14 (Sonoma) yoki undan yangi versiya
- Claude Pro ($20/oy) yoki Max ($100/oy) obunasi — Cowork bepul rejada mavjud emas
- Google akkaunt (bepul Google Workspace yetarli)

**1-qadam: Claude Desktop o'rnatish (2 daq)**

1. claude.ai/download saytini oching
2. "Download for macOS" tugmasini bosing
3. Yuklab olingan faylni oching
4. Claude.app'ni Applications papkasiga torting
5. Applications'dan Claude Desktop'ni ishga tushiring
6. Pro yoki Max obunali akkauntingizga kiring

Kirganingizdan so'ng oyna yuqorisida uchta varaq ko'rasiz: **Chat**, **Cowork** va **Code**. **Cowork** varaqini bosing — bu agent rejimi.

**2-qadam: Google Workspace CLI o'rnatish (3 daq)**

Google Workspace CLI — Google'ning rasmiy vositasi (github.com/googleworkspace/cli). U Google Docs, Sheets, Drive, Gmail va Calendar bilan buyruq satri orqali ishlash imkonini beradi. Claude Cowork fayllaringizga kirish uchun undan foydalanadi.

Terminal'ni (Mac'dagi "Terminal" ilovasi) oching va bitta buyruqni bajaring:

```bash
npm install -g @googleworkspace/cli
```

Agar npm o'rnatilmagan bo'lsa, avval nodejs.org saytidan Node.js'ni o'rnating.

O'rnatilganini tekshiring:
```bash
gws --version
```

Agar versiya raqamini ko'rsangiz — hammasi o'rnatilgan.

**3-qadam: Google akkaunt avtorizatsiyasi (3 daq)**

Endi Google akkauntingizni ulash kerak. Terminal'da bajaring:

```bash
gws auth setup
```

Bu buyruq hammasini avtomatik qiladi:
- Siz uchun Google Cloud loyihasi yaratadi
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

Agar Google Drive'dagi fayllaringiz ro'yxatini ko'rsangiz — ulanish ishlayapti.

Endi Claude Desktop'ga o'ting, Cowork varag'ini oching va yozing:
> "Google Drive'dagi so'nggi fayllarimni gws buyrug'i orqali ko'rsat"

Claude buyruqni bajarishi va fayllar ro'yxatini ko'rsatishi kerak.

**Ma'lumotlar xavfsizligi**

Muhim jihat: Google Workspace CLI orqali Claude sizning Google akkauntingizga kirish huquqiga ega bo'ladi. Bilishingiz kerak bo'lgan narsalar:

- Claude Cowork izolyatsiyalangan muhitda (sandbox) ishlaydi — ma'lumotlar seansdan tashqariga chiqmaydi
- `gws` Google'ning standart OAuth-avtorizatsiyasidan foydalanadi — mobil ilovalar bilan bir xil mexanizm
- `gws`ning qaysi xizmatlarga kirish huquqi borligini siz nazorat qilasiz (`gws auth login`da tanlaysiz)
- **Ulash xavfsiz:** ish hujjatlari, hisobotlar, umumlashtirilgan ma'lumotli jadvallar
- **Ulash tavsiya etilmaydi:** mijozlarning shaxsiy ma'lumotlari (ism + telefon + pasport ma'lumotlari), NDA bilan himoyalangan moliyaviy hisobotlar, parollar va kirish kalitlari

Tavsiya: Google Drive'da Claude bilan ishlash uchun alohida papka yarating va unda faqat AI orqali tahlil qilish xavfsiz bo'lgan fayllarni saqlang.

### Xulosa (30 sek)

Ajoyib! Endi sizda Google Workspace ulangan Claude Cowork sozlangan. E'tibor bering, bu qanchalik oson bo'ldi — Terminal'da ikkita buyruq va Claude allaqachon hujjatlaringizni ko'ra olyapti. Keyingi darsda biz CLAUDE.md yaratamiz — bu fayl Claude'ni oddiy universal AI emas, shaxsiy yordamchingizga aylantiradi.

## Matnli qo'llanma

### Talablar

| Parametr | Talab |
|----------|-------|
| Kompyuter | Apple Silicon (M1/M2/M3+) li Mac |
| OT | macOS 14 (Sonoma) yoki yangi |
| Obuna | Claude Pro ($20/oy) yoki Max ($100/oy) |
| Google | Bepul Google akkaunt (Workspace shart emas) |
| Node.js | gws CLI'ni npm orqali o'rnatish uchun |

### Bosqichma-bosqich yo'riqnoma

#### 1. Claude Desktop o'rnatish

1. claude.ai/download sahifasiga o'ting
2. macOS versiyasini yuklab oling
3. Claude.app'ni Applications'ga torting
4. Ishga tushiring va akkauntga kiring
5. Oyna yuqorisidagi **Cowork** varag'ini tanlang

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
# Rust (cargo) orqali
cargo install --git https://github.com/googleworkspace/cli --locked

# Nix orqali
nix run github:googleworkspace/cli
```

#### 3. Avtorizatsiya

```bash
# Boshlang'ich sozlash (Google Cloud loyihasini avtomatik yaratadi)
gws auth setup

# Xizmatlarni tanlash bilan avtorizatsiya
gws auth login
```

`gws auth login`da ulamoqchi bo'lgan xizmatlarni tanlang:
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

Keyin Claude Desktop'da Cowork varag'ida:
> "Google Drive'dagi fayllarimni gws orqali ko'rsat"

Agar Claude fayllar ro'yxatini ko'rsatsa — sozlash tugallangan.

### Taqqoslash: nima uchun gws, uchinchi tomon vositalari emas

| Parametr | Google Workspace CLI (gws) | Uchinchi tomon MCP-serverlari |
|----------|---------------------------|-------------------------------|
| Ishlab chiqaruvchi | Google (rasmiy) | Hamjamiyat |
| O'rnatish | 1 ta buyruq (`npm install`) | Reponi klonlash, env sozlash |
| OAuth sozlash | Avtomatik (`gws auth setup`) | Qo'lda (Google Cloud Console) |
| Qo'llab-quvvatlanadigan API'lar | Barcha Google Workspace API | Cheklangan to'plam |
| Yangilanishlar | Google'dan | Muallif qaroriga bog'liq |

### Ma'lumotlar xavfsizligi

| Xavfsiz | Tavsiya etilmaydi |
|---------|-------------------|
| Ish hisobotlari | Mijozlarning shaxsiy ma'lumotlari |
| Umumlashtirilgan jadvallar | NDA bilan himoyalangan moliyaviy hisobotlar |
| Hujjat shablonlari | Parollar va kirish kalitlari |
| Xat qoralmalari | Tibbiy ma'lumotli hujjatlar |

**Tavsiya:** Google Drive'da Claude bilan ishlash uchun alohida papka yarating.

### Muammolarni bartaraf etish

| Muammo | Yechim |
|--------|--------|
| `npm: command not found` | nodejs.org saytidan Node.js o'rnating |
| `gws: command not found` | O'rnatishdan keyin Terminal'ni qayta ishga tushiring |
| Avtorizatsiya xatosi | `gws auth login`ni qaytadan bajaring |
| Claude fayllarni ko'rmayapti | Terminal'da `gws drive files list`ni tekshiring |
| Docs/Sheets'ga kirish yo'q | `gws auth login`da kerakli xizmatlarni tanlang |

## Asosiy xulosalar

1. **Cowork uchun Mac** (Apple Silicon, macOS 14+) va **Pro yoki Max obunasi** talab etiladi. Bepul rejada agent rejimi mavjud emas
2. **Google Workspace CLI** — Google'ning rasmiy vositasi. O'rnatish: `npm install -g @googleworkspace/cli`, avtorizatsiya: `gws auth setup` va `gws auth login`. Uchinchi tomon MCP-serverlarini sozlashdan ancha oson
3. **Xavfsizlik:** Claude sandbox'da ishlaydi, `gws` esa Google'ning standart OAuth-avtorizatsiyasidan foydalanadi. AI bilan ishlash uchun alohida papka yarating va shaxsiy ma'lumotli hujjatlarni ulamang
