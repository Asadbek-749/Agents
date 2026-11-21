# -*- coding: utf-8 -*-
"""
Word kursi, 01-dars: "Word'da faylni tóǵri saqlaş"
Bu skript 3 ta fayl yaratadi (skript turgan papkaning bir poǵona yuqorisiga):
  - dars-rejasi.docx
  - dars-rejasi.html
  - topshiriq-varaqasi.docx

Ishga tushiriş:
  pip install python-docx
  python3 dars_rejasi.py
"""
import html
import os

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

# ---------------------------------------------------------------- brend
ASOSIY = "1E3A8A"
URGU = "F59E0B"
MATN = "1F2937"
OCH_FON = "F3F4F6"
TOGRI = "16A34A"
XATO = "DC2626"
SHRIFT = "Arial"  # Word uçun zaxira shrift: har bir kompyuterda bor
IMZO = "Ustoz Shodiyev · Kompyuter savodxonligi va AI"

PAPKA = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------- mazmun
SARLAVHA = "Word'da faylni tóǵri saqlaş"
KURS = "Microsoft Word · 01-dars"

MALUMOT = [
    ("Mavzu", SARLAVHA),
    ("Daraja", "Boşlanǵiç"),
    ("Davomiyligi", "80 daqiqa"),
    ("Auditoriya", "Óquvçilar va kattalar (tadbirkorlar, davlat xodimlari)"),
]

MAQSADLAR = [
    "Yangi hujjatni kerakli papkaga, tuşunarli nom bilan saqlay oladi (Save As yoki F12).",
    "Save va Save As farqini tuşuntiradi, hujjatni boşqa nom yoki PDF formatda nusxa qilib saqlay oladi.",
    "Avtomatik saqlaşni (AutoRecover) yoqadi va saqlanmay qolgan hujjatni tiklay oladi.",
]

KERAKLI = [
    "Microsoft Word 2016, 2019, 2021 yoki Microsoft 365 (ingliz yoki rus interfeysi).",
    "Har bir kompyuterda «Documents» («Документы») papkasi.",
    "Óqituvçi kompyuteri va proyektor.",
    "Internet şart emas. Faqat OneDrive haqida gapirilsa kerak bóladi.",
]

BOSQICHLAR = [
    ("0–10", "Kiriş va motivatsiya",
     "Hikoya aytadi: tadbirkor 2 soat şartnoma yozdi, svet óçdi, hammasi yóqoldi. "
     "Sóraydi: «Kim hujjatini yóqotgan? Nima uçun yóqoldi?»",
     "Óz tajribasini aytadi, muammoni tuşunadi."),
    ("10–30", "Yangi mavzu",
     "Proyektorda kórsatadi: Save va Save As farqi, F12, papka tanlaş, fayl nomi qoidalari, formatlar (.docx, .pdf).",
     "Kuzatadi, daftarga 3 ta tugmani yozadi: F12, Ctrl+S, Save As."),
    ("30–50", "Birga maşq",
     "«Ariza» hujjatini birga yaratadi: papka oçiş, nom beriş, Ctrl+S, PDF qiliş, AutoRecover sozlaş.",
     "Óqituvçi bilan birga qadamma-qadam bajaradi."),
    ("50–70", "Mustaqil iş",
     "Amaliy topşiriqni beradi, sinfni aylanib yordam beradi, xatolarni kórsatadi.",
     "Topşiriqni óz darajasida bajaradi (oson, órta yoki murakkab)."),
    ("70–80", "Yakun",
     "Tekşiriş savollarini beradi, uyga vazifani tuşuntiradi.",
     "Savollarga javob beradi, uyga vazifani yozib oladi."),
]

ATAMALAR = [
    ("Fayl", "Kompyuterdagi bitta hujjat. Xuddi papka içidagi bitta qoǵoz varaq."),
    ("Papka", "Fayllar saqlanadigan joy. Xuddi ofisdagi javon yoki hujjatlar papkasi."),
    ("Saqlaş (Save)", "Hujjatni kompyuter xotirasiga yozib qóyiş. Saqlanmagan matn doskaga bór bilan "
                      "yozilgan yozuvga óxşaydi: óçirilsa, yóqoladi."),
    ("Format (kengaytma)", "Fayl nomidan keyingi qóşimça: .docx, .pdf. Bitta taomni likopçada yoki "
                           "paketda berişga óxşaydi: mazmuni bir, kórinişi va işlatilişi boşqa."),
    ("AutoRecover", "Word har bir neça daqiqada yaşirin zaxira nusxa olib turadi. Bu svet óçganda "
                    "yordam beradi, lekin oddiy saqlaşning órnini bosmaydi."),
]

QADAMLAR = [
    {
        "nom": "Birinçi marta saqlaş (Save As)",
        "bosish": "File (Файл) → Save As (Сохранить как) → Browse (Обзор). Tezroq yól: klaviaturada F12.",
        "chiqadi": "«Save As» oynasi oçiladi: çapda papkalar, pastda «File name» (Имя файла) va "
                   "«Save as type» (Тип файла) qatorlari.",
        "xato": "Óquvçi papkani tanlamasdan Save bosadi va fayl qayerga ketganini bilmaydi.",
        "tuzatish": "Avval oynaning çap tomonidan «Documents» yoki «Desktop» ni tanlang, keyin saqlang. "
                    "Fayl yóqolgan bólsa: File → Open → Recent (Последние) da topiladi.",
    },
    {
        "nom": "Papka tanlaş va yangi papka oçiş",
        "bosish": "Save As oynasida kerakli joyni tanlang → yuqoridagi «New folder» (Новая папка) → "
                  "nom yozing, masalan «Word darslari» → Enter → papkani ikki marta bosib içiga kiring.",
        "chiqadi": "Yangi papka róyxatda paydo bóladi, oyna yuqorisidagi manzil qatorida uning nomi kórinadi.",
        "xato": "Papka yaratiladi, lekin içiga kirilmaydi. Fayl papkaning taşqarisida saqlanadi.",
        "tuzatish": "Save bosişdan oldin yuqoridagi manzil qatorida papka nomi turganini tekşiring.",
    },
    {
        "nom": "Faylga tóǵri nom beriş",
        "bosish": "«File name» (Имя файла) qatoriga nom yozing. Nom mazmunni aytsin va sanasi bólsin: "
                  "Ariza_Karimov_2026-11-21. «Document1», «Yangi», «111» kabi nomlar yomon.",
        "chiqadi": "Saqlangandan keyin Word oynasining eng yuqorisida yangi nom kórinadi.",
        "xato": 'Nomga \\ / : * ? " < > | belgilari yoziladi yoki «.docx» qólda yozilib, kengaytma buziladi.',
        "tuzatish": "Bu belgilar órniga pastki çiziq (_) yoki tire (-) işlating. Kengaytmani yozmang: "
                    "Word uni ózi qóşadi, format «Save as type» róyxatida tanlanadi.",
    },
    {
        "nom": "Keyingi saqlaşlar: Save (Ctrl+S)",
        "bosish": "Hujjatni ózgartirgaç Ctrl+S ni bosing yoki yuqori çap burçakdagi disket belgisini bosing.",
        "chiqadi": "Heç qanday oyna çiqmaydi. Word faylni şu nom va şu joyda yangilaydi.",
        "xato": "Óquvçi har safar Save As bosib, «Ariza1», «Ariza2», «Ariza3» kabi keraksiz nusxalar yaratadi.",
        "tuzatish": "Qoida: birinçi marta Save As, keyin faqat Ctrl+S. Har 5–10 daqiqada Ctrl+S bosiş odat bólsin.",
    },
    {
        "nom": "Nusxa yoki PDF formatda saqlaş",
        "bosish": "File → Save As → Browse → «Save as type» (Тип файла) róyxatidan PDF ni tanlang → Save.",
        "chiqadi": "Papkada ikki fayl bóladi: Ariza.docx (tahrirlaş uçun) va Ariza.pdf (yuboriş va çop etiş uçun).",
        "xato": "PDF yaratilgaç, asl .docx faylni keraksiz deb óçirib yuboradi.",
        "tuzatish": ".docx asl nusxa, uni doim saqlang. PDF faqat yuboriş uçun: uni Word'da qulay tahrirlab bólmaydi.",
    },
    {
        "nom": "Avtomatik saqlaşni yoqiş (AutoRecover)",
        "bosish": "File → Options (Параметры) → Save (Сохранение) → «Save AutoRecover information every» "
                  "belgisini qóying, raqamni 10 dan 5 ga ózgartiring → OK.",
        "chiqadi": "Endi Word har 5 daqiqada yaşirin zaxira nusxa oladi.",
        "xato": "AutoRecover yoqilgaç, óquvçi Ctrl+S bosmay qóyadi.",
        "tuzatish": "AutoRecover faqat favqulodda holat (svet óçişi, kompyuter qotişi) uçun. "
                    "Asosiy saqlaş baribir Ctrl+S.",
    },
    {
        "nom": "Saqlanmagan hujjatni tiklaş",
        "bosish": "Word'ni qayta oçing: çapda «Document Recovery» paneli çiqadi. Çiqmasa: File → Info (Сведения) → "
                  "Manage Document (Управление документом) → Recover Unsaved Documents "
                  "(Восстановить несохраненные документы).",
        "chiqadi": "Saqlanmay qolgan fayllar róyxati oçiladi.",
        "xato": "Tiklangan faylni oçib, saqlamasdan yopadi va u yana yóqoladi.",
        "tuzatish": "Tiklangan faylni darhol Save As bilan óz papkangizga saqlang.",
    },
    {
        "nom": "Word yopilayotganda çiqadigan savol",
        "bosish": "Word'ni yopganingizda sóraydi: «Want to save your changes?». Tugmalar: Save / Don't Save / "
                  "Cancel (Сохранить / Не сохранять / Отмена).",
        "chiqadi": "Save bossangiz saqlanadi, Don't Save bossangiz oxirgi ózgarişlar yóqoladi, Cancel oynaga qaytaradi.",
        "xato": "Şoşilib «Don't Save» bosiladi.",
        "tuzatish": "Ikkilansangiz Save yoki Cancel ni bosing. «Don't Save» ni faqat ózgarişlar kerak bólmasa bosing.",
    },
]

FORMATLAR = [
    (".docx", "Oddiy Word hujjati. Tahrirlaş uçun asosiy format."),
    (".pdf", "Óqiş, yuboriş va çop etiş uçun. Hamma qurilmada bir xil kórinadi."),
    (".doc", "Eski Word (2003 va undan oldingi) uçun. Faqat juda eski kompyuterga yuborilsa."),
    (".dotx", "Şablon: bir xil hujjatlarni (ariza, buyruq) tez yaratiş uçun."),
]

TOPSHIRIQ_VAZIYAT = ("Vaziyat: siz idorada yoki óz dókoningizda işlaysiz va rahbarga ariza yozişingiz kerak. "
                     "Ariza yóqolmasligi, tez topilişi va elektron poçta orqali yuborilişi kerak.")

TOPSHIRIQLAR = [
    ("Oson", [
        "Yangi hujjatga 3 qatorli ariza yozing: kimga, kimdan, nima sóraysiz.",
        "«Documents» içida «Word darslari» papkasini yarating.",
        "Arizani F12 orqali «Ariza_Familiyangiz» nomi bilan şu papkaga saqlang.",
    ]),
    ("Órta", [
        "Arizaga sana va imzo qatorini qóşing, Ctrl+S bilan saqlang.",
        "Şu arizani PDF formatda ham saqlang. Papkada 2 ta fayl bólsin: .docx va .pdf.",
    ]),
    ("Murakkab", [
        "AutoRecover vaqtini 5 daqiqaga sozlang.",
        "«Word darslari» içida «Arizalar» va «Hisobotlar» papkalarini yarating.",
        "Arizani Save As bilan «Arizalar» papkasiga «Ariza_Familiya_2026-11-21» nomi bilan saqlang.",
        "Yangi hujjat oçib, 1 gap yozing va Word'ni yopişga urining. Çiqqan oynada tóǵri tugmani tanlab, "
        "hujjatni «Hisobotlar» papkasiga saqlang.",
    ]),
]

SAVOLLAR = [
    ("Save va Save As farqi nima?",
     "Save faylni şu nom va şu joyda yangilaydi. Save As yangi nom, joy yoki formatda nusxa yaratadi; "
     "birinçi marta saqlaşda ham Save As işlaydi."),
    ("Save As oynasini qaysi tugma bilan tez oçiş mumkin?", "F12."),
    ("Nima uçun «Document1» yomon fayl nomi?",
     "U hujjat mazmunini aytmaydi, keyin faylni topiş qiyin bóladi, bir xil nomlar kópayib ketadi."),
    ("Hujjatni hamma joyda bir xil kórinadigan qilib yuboriş uçun qaysi formatda saqlaysiz?", "PDF."),
    ("Svet óçib, hujjat saqlanmay qolsa nima qilasiz?",
     "Word'ni qayta oçib Document Recovery paneliga qarayman yoki File → Info → Manage Document → "
     "Recover Unsaved Documents ni bosaman. Topilgan faylni darhol Save As qilaman."),
]

UYGA_VAZIFA = ("Óz işingiz yoki óqişingiz uçun 1 ta haqiqiy hujjat yozing (ariza, tuşuntiriş xati, narxlar róyxati). "
               "«Documents» içida tartibli papka yarating (masalan: Iş → Arizalar). Faylni qoidaga mos nom bilan "
               ".docx va .pdf formatda saqlang. Papka oçiq turgan ekranning rasmini (Win + Shift + S) óqituvçiga yuboring.")

MEZONLAR = [
    ("Papka tuzilmasi tartibli (kamida 2 poǵona)", "2"),
    ("Fayl nomi qoidaga mos: mazmun + sana, taqiqlangan belgilarsiz", "3"),
    (".docx va .pdf fayllar ikkalasi bor", "3"),
    ("Ekran rasmi yuborilgan, papka va fayllar kórinadi", "2"),
    ("Jami", "10"),
]

ESLATMALAR = [
    "Eng kóp qiynaladigan joy: óquvçi Save As oynasida qaysi papkada turganini tuşunmaydi. "
    "Manzil qatorini proyektorda kattalaştirib kórsating.",
    "Kattalar kópinçha hamma narsani Desktop'ga saqlaşga órganib qolgan. Tartibsiz Desktop rasmini "
    "kórsatib, «javon» misolini eslating.",
    "Sinfda rus va ingliz interfeysli kompyuterlar aralaş bólsa, menyu nomlarini doskaga ikki tilda yozib qóying.",
    "Word 2016 va keyingilarida Save As bosilganda avval kulrang sahifa çiqadi, Browse ni bosiş kerak. "
    "F12 esa oynani darhol oçadi: buni alohida taʼkidlang.",
    "Microsoft 365 va OneDrive ulangan bólsa, yuqorida «AutoSave» (Автосохранение) tugmasi bor: u faylni bulutda "
    "real vaqtda saqlaydi. Qisqa aytib óting, lekin asosiy odat baribir Ctrl+S.",
    "Qóşimça vaqt bólsa: Explorer'da fayl nomini F2 bilan ózgartiriş va View → File name extensions orqali "
    "kengaytmani kórsatişni órgating.",
]

ESDA_TUTING = [
    ("F12", "Save As oynasini oçadi"),
    ("Ctrl + S", "Saqlaydi (keyingi saqlaşlar)"),
    ("File → Save As → PDF", "PDF nusxa yaratadi"),
    ("File → Options → Save", "AutoRecover sozlamasi"),
]

NATIJA_DARAXT = """Documents
└── Word darslari
    ├── Ariza_Familiya.docx
    ├── Ariza_Familiya.pdf
    ├── Arizalar
    │   └── Ariza_Familiya_2026-11-21.docx
    └── Hisobotlar
        └── Hisobot_Familiya.docx"""

OZINI_TEKSHIR = [
    "Fayllarim qaysi papkada ekanini bilaman.",
    "Fayl nomlarida «Document1» yóq.",
    "Papkada .docx va .pdf fayllar bor.",
    "AutoRecover 5 daqiqaga sozlangan.",
]


# ---------------------------------------------------------------- Word yordamçilari
def rgb(hex_):
    return RGBColor.from_string(hex_)


def katakni_boya(cell, hex_):
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hex_)
    tc_pr.append(shd)


def shriftni_qoy(run, size=None, bold=None, color=None, font=SHRIFT):
    run.font.name = font
    rpr = run._element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.append(rfonts)
    for k in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rfonts.set(qn(k), font)
    if size:
        run.font.size = Pt(size)
    if bold is not None:
        run.bold = bold
    if color:
        run.font.color.rgb = rgb(color)


def hujjat_yarat():
    doc = Document()
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Cm(21), Cm(29.7)
    sec.left_margin = sec.right_margin = Cm(2)
    sec.top_margin = sec.bottom_margin = Cm(1.8)

    st = doc.styles["Normal"]
    st.font.name = SHRIFT
    st.font.size = Pt(11)
    st.font.color.rgb = rgb(MATN)
    st.element.rPr.rFonts.set(qn("w:eastAsia"), SHRIFT)
    st.paragraph_format.space_after = Pt(4)
    st.paragraph_format.line_spacing = 1.15

    for name, size in (("Title", 24), ("Heading 1", 16), ("Heading 2", 13), ("Heading 3", 12)):
        s = doc.styles[name]
        s.font.name = SHRIFT
        s.font.size = Pt(size)
        s.font.bold = True
        s.font.color.rgb = rgb(ASOSIY if name != "Heading 3" else MATN)
        rpr = s.element.get_or_add_rPr()
        rf = rpr.find(qn("w:rFonts"))
        if rf is None:
            rf = OxmlElement("w:rFonts")
            rpr.append(rf)
        for k in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
            rf.set(qn(k), SHRIFT)
        for a in ("w:asciiTheme", "w:hAnsiTheme", "w:eastAsiaTheme", "w:cstheme"):
            if rf.get(qn(a)) is not None:
                del rf.attrib[qn(a)]
        s.paragraph_format.space_before = Pt(14 if name == "Heading 1" else 8)
        s.paragraph_format.space_after = Pt(6)

    # pastki imzo
    fp = sec.footer.paragraphs[0]
    fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = fp.add_run(IMZO)
    shriftni_qoy(r, size=9, color=ASOSIY)
    return doc


def jadval(doc, sarlavhalar, qatorlar, kengliklar=None, oxirgi_qalin=False):
    t = doc.add_table(rows=1, cols=len(sarlavhalar))
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, s in enumerate(sarlavhalar):
        c = t.rows[0].cells[i]
        katakni_boya(c, ASOSIY)
        p = c.paragraphs[0]
        shriftni_qoy(p.add_run(s), size=10, bold=True, color="FFFFFF")
    for n, q in enumerate(qatorlar):
        cells = t.add_row().cells
        for i, v in enumerate(q):
            if n % 2 == 1:
                katakni_boya(cells[i], OCH_FON)
            p = cells[i].paragraphs[0]
            qalin = oxirgi_qalin and n == len(qatorlar) - 1
            shriftni_qoy(p.add_run(v), size=10, bold=qalin or None)
    if kengliklar:
        for row in t.rows:
            for i, w in enumerate(kengliklar):
                row.cells[i].width = Cm(w)
    doc.add_paragraph()
    return t


def qalin_label(doc, label, matn, rang=ASOSIY):
    p = doc.add_paragraph()
    shriftni_qoy(p.add_run(label + " "), bold=True, color=rang)
    shriftni_qoy(p.add_run(matn))
    return p


def ogohlantirish_quti(doc, xato, tuzatish):
    t = doc.add_table(rows=1, cols=1)
    t.style = "Table Grid"
    c = t.rows[0].cells[0]
    katakni_boya(c, OCH_FON)
    p = c.paragraphs[0]
    shriftni_qoy(p.add_run("Keng tarqalgan xato: "), bold=True, color=XATO)
    shriftni_qoy(p.add_run(xato), size=10)
    p2 = c.add_paragraph()
    shriftni_qoy(p2.add_run("Tuzatiş: "), bold=True, color=TOGRI)
    shriftni_qoy(p2.add_run(tuzatish), size=10)
    doc.add_paragraph()


def muqova_sarlavha(doc, kichik, katta):
    p = doc.add_paragraph()
    shriftni_qoy(p.add_run(kichik.upper()), size=10, bold=True, color=URGU)
    doc.add_paragraph(katta, style="Title")


# ---------------------------------------------------------------- 1) dars-rejasi.docx
def dars_rejasi_docx(yol):
    doc = hujjat_yarat()
    muqova_sarlavha(doc, KURS, SARLAVHA)

    doc.add_heading("1. Mavzu va daraja", level=1)
    jadval(doc, ["Kórsatkiç", "Qiymat"], MALUMOT, [4.5, 12.5])

    doc.add_heading("2. Dars maqsadi", level=1)
    doc.add_paragraph("Dars oxirida óquvçi:")
    for m in MAQSADLAR:
        doc.add_paragraph(m, style="List Number")

    doc.add_heading("3. Kerakli narsalar", level=1)
    for k in KERAKLI:
        doc.add_paragraph(k, style="List Bullet")

    doc.add_heading("4. Dars bosqiçlari", level=1)
    jadval(doc, ["Vaqt (daq.)", "Bosqiç", "Óqituvçi nima qiladi", "Óquvçi nima qiladi"],
           BOSQICHLAR, [2, 3, 6.5, 5.5])

    doc.add_heading("5. Qadamma-qadam kórsatma", level=1)
    doc.add_heading("Yangi atamalar", level=2)
    jadval(doc, ["Atama", "Sodda tuşuntiriş"], ATAMALAR, [4, 13])
    for i, q in enumerate(QADAMLAR, 1):
        doc.add_heading(f"{i}-qadam. {q['nom']}", level=3)
        qalin_label(doc, "Qayerni bosiş:", q["bosish"])
        qalin_label(doc, "Nima çiqadi:", q["chiqadi"])
        ogohlantirish_quti(doc, q["xato"], q["tuzatish"])
        if i == 5:
            doc.add_paragraph("Asosiy formatlar:").runs[0].bold = True
            jadval(doc, ["Format", "Qaçon işlatiladi"], FORMATLAR, [3, 14])

    doc.add_heading("6. Amaliy topşiriq", level=1)
    doc.add_paragraph(TOPSHIRIQ_VAZIYAT)
    for daraja, qadamlar in TOPSHIRIQLAR:
        doc.add_heading(f"{daraja} daraja", level=3)
        for q in qadamlar:
            doc.add_paragraph(q, style="List Number")
    doc.add_paragraph("Natija qanday kórinişi kerak (murakkab daraja):").runs[0].bold = True
    p = doc.add_paragraph()
    shriftni_qoy(p.add_run(NATIJA_DARAXT), size=10, font="Consolas")

    doc.add_heading("7. Tekşiriş savollari", level=1)
    for i, (s, j) in enumerate(SAVOLLAR, 1):
        p = doc.add_paragraph()
        shriftni_qoy(p.add_run(f"{i}. {s}"), bold=True)
        qalin_label(doc, "Javob:", j, rang=TOGRI)

    doc.add_heading("8. Uyga vazifa", level=1)
    doc.add_paragraph(UYGA_VAZIFA)
    jadval(doc, ["Baholaş mezoni", "Ball"], MEZONLAR, [14, 3], oxirgi_qalin=True)

    doc.add_heading("9. Óqituvçi uçun eslatma", level=1)
    for e in ESLATMALAR:
        doc.add_paragraph(e, style="List Bullet")

    doc.save(yol)


# ---------------------------------------------------------------- 2) topshiriq-varaqasi.docx
def topshiriq_docx(yol):
    doc = hujjat_yarat()
    muqova_sarlavha(doc, KURS + " · Amaliy topşiriq", SARLAVHA)
    p = doc.add_paragraph()
    shriftni_qoy(p.add_run("Ism, familiya: ______________________________    Sana: ____________"))

    doc.add_heading("Esda tuting", level=2)
    jadval(doc, ["Tugma / yól", "Nima qiladi"], ESDA_TUTING, [6, 11])

    doc.add_heading("Topşiriq", level=2)
    doc.add_paragraph(TOPSHIRIQ_VAZIYAT)
    for daraja, qadamlar in TOPSHIRIQLAR:
        doc.add_heading(f"{daraja} daraja", level=3)
        for q in qadamlar:
            doc.add_paragraph("☐  " + q)

    doc.add_heading("Natija qanday kórinişi kerak", level=2)
    p = doc.add_paragraph()
    shriftni_qoy(p.add_run(NATIJA_DARAXT), size=10, font="Consolas")

    doc.add_heading("Ózingizni tekşiring", level=2)
    for q in OZINI_TEKSHIR:
        doc.add_paragraph("☐  " + q)

    doc.add_heading("Qoida", level=2)
    t = doc.add_table(rows=1, cols=1)
    t.style = "Table Grid"
    c = t.rows[0].cells[0]
    katakni_boya(c, OCH_FON)
    shriftni_qoy(c.paragraphs[0].add_run(
        "Birinçi marta: Save As (F12). Keyin: faqat Ctrl+S. Har 5–10 daqiqada Ctrl+S!"),
        size=12, bold=True, color=ASOSIY)
    doc.save(yol)


# ---------------------------------------------------------------- 3) dars-rejasi.html
def e(s):
    return html.escape(s)


def html_jadval(sarlavhalar, qatorlar, oxirgi_qalin=False):
    th = "".join(f"<th>{e(s)}</th>" for s in sarlavhalar)
    rows = []
    for n, q in enumerate(qatorlar):
        cls = ' class="jami"' if oxirgi_qalin and n == len(qatorlar) - 1 else ""
        rows.append(f"<tr{cls}>" + "".join(f"<td>{e(v)}</td>" for v in q) + "</tr>")
    return f'<div class="jw"><table><thead><tr>{th}</tr></thead><tbody>{"".join(rows)}</tbody></table></div>'


def dars_rejasi_html(yol):
    b = []
    b.append(f'<header><p class="kurs">{e(KURS)}</p><h1>{e(SARLAVHA)}</h1>'
             f'<p class="meta">Boşlanǵiç · 80 daqiqa · Óquvçilar va kattalar</p></header>')
    b.append("<nav><b>Mundarija:</b> " + " · ".join(
        f'<a href="#b{i}">{e(t)}</a>' for i, t in enumerate(
            ["Mavzu", "Maqsad", "Kerakli narsalar", "Bosqiçlar", "Kórsatma",
             "Topşiriq", "Savollar", "Uyga vazifa", "Eslatma"], 1)) + "</nav>")

    b.append('<section id="b1"><h2>1. Mavzu va daraja</h2>' + html_jadval(["Kórsatkiç", "Qiymat"], MALUMOT) + "</section>")
    b.append('<section id="b2"><h2>2. Dars maqsadi</h2><p>Dars oxirida óquvçi:</p><ol>'
             + "".join(f"<li>{e(m)}</li>" for m in MAQSADLAR) + "</ol></section>")
    b.append('<section id="b3"><h2>3. Kerakli narsalar</h2><ul>'
             + "".join(f"<li>{e(k)}</li>" for k in KERAKLI) + "</ul></section>")
    b.append('<section id="b4"><h2>4. Dars bosqiçlari</h2>'
             + html_jadval(["Vaqt (daq.)", "Bosqiç", "Óqituvçi nima qiladi", "Óquvçi nima qiladi"], BOSQICHLAR)
             + "</section>")

    s = ['<section id="b5"><h2>5. Qadamma-qadam kórsatma</h2><h3>Yangi atamalar</h3>',
         html_jadval(["Atama", "Sodda tuşuntiriş"], ATAMALAR)]
    for i, q in enumerate(QADAMLAR, 1):
        s.append(f'<div class="qadam"><h3><span class="raqam">{i}</span>{e(q["nom"])}</h3>'
                 f'<p><b>Qayerni bosiş:</b> {e(q["bosish"])}</p>'
                 f'<p><b>Nima çiqadi:</b> {e(q["chiqadi"])}</p>'
                 f'<div class="quti"><p><b class="xato">Keng tarqalgan xato:</b> {e(q["xato"])}</p>'
                 f'<p><b class="togri">Tuzatiş:</b> {e(q["tuzatish"])}</p></div></div>')
        if i == 5:
            s.append("<h3>Asosiy formatlar</h3>" + html_jadval(["Format", "Qaçon işlatiladi"], FORMATLAR))
    s.append("</section>")
    b.append("".join(s))

    t = [f'<section id="b6"><h2>6. Amaliy topşiriq</h2><p>{e(TOPSHIRIQ_VAZIYAT)}</p><div class="darajalar">']
    for daraja, qadamlar in TOPSHIRIQLAR:
        t.append(f'<div class="daraja"><h3>{e(daraja)}</h3><ol>'
                 + "".join(f"<li>{e(q)}</li>" for q in qadamlar) + "</ol></div>")
    t.append(f'</div><h3>Natija qanday kórinişi kerak</h3><pre>{e(NATIJA_DARAXT)}</pre></section>')
    b.append("".join(t))

    b.append('<section id="b7"><h2>7. Tekşiriş savollari</h2>' + "".join(
        f'<details><summary>{i}. {e(sv)}</summary><p><b class="togri">Javob:</b> {e(j)}</p></details>'
        for i, (sv, j) in enumerate(SAVOLLAR, 1)) + "</section>")
    b.append(f'<section id="b8"><h2>8. Uyga vazifa</h2><p>{e(UYGA_VAZIFA)}</p>'
             + html_jadval(["Baholaş mezoni", "Ball"], MEZONLAR, oxirgi_qalin=True) + "</section>")
    b.append('<section id="b9"><h2>9. Óqituvçi uçun eslatma</h2><ul>'
             + "".join(f"<li>{e(x)}</li>" for x in ESLATMALAR) + "</ul></section>")

    css = f"""
:root{{--asosiy:#{ASOSIY};--urgu:#{URGU};--matn:#{MATN};--fon:#{OCH_FON};--togri:#{TOGRI};--xato:#{XATO}}}
*{{box-sizing:border-box}}
body{{margin:0;background:#fff;color:var(--matn);font:16px/1.6 Inter,Arial,sans-serif}}
main{{max-width:900px;margin:0 auto;padding:0 16px 40px}}
header{{background:var(--asosiy);color:#fff;padding:32px 20px;margin:0 -16px 20px}}
header .kurs{{color:var(--urgu);font-weight:700;letter-spacing:.06em;text-transform:uppercase;margin:0;font-size:13px}}
h1,h2,h3{{font-family:Montserrat,Arial,sans-serif;line-height:1.25}}
h1{{margin:6px 0;font-size:30px}}
header .meta{{margin:0;opacity:.85}}
h2{{color:var(--asosiy);border-bottom:3px solid var(--urgu);padding-bottom:4px;margin-top:36px}}
h3{{font-size:17px;margin:20px 0 8px}}
nav{{background:var(--fon);padding:12px 14px;border-radius:8px;font-size:14px}}
nav a{{color:var(--asosiy)}}
.jw{{overflow-x:auto}}
table{{border-collapse:collapse;width:100%;font-size:14px;margin:8px 0}}
th{{background:var(--asosiy);color:#fff;text-align:left}}
th,td{{border:1px solid #d1d5db;padding:8px 10px;vertical-align:top}}
tbody tr:nth-child(even) td{{background:var(--fon)}}
tr.jami td{{font-weight:700}}
.qadam{{border-left:4px solid var(--asosiy);padding:2px 0 2px 14px;margin:18px 0}}
.raqam{{display:inline-block;background:var(--urgu);color:#fff;border-radius:50%;width:26px;height:26px;
text-align:center;line-height:26px;margin-right:8px;font-size:14px}}
.quti{{background:var(--fon);border-radius:8px;padding:4px 14px}}
.xato{{color:var(--xato)}} .togri{{color:var(--togri)}}
.darajalar{{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:12px}}
.daraja{{background:var(--fon);border-radius:8px;padding:2px 14px;border-top:4px solid var(--urgu)}}
pre{{background:var(--fon);padding:12px;border-radius:8px;overflow-x:auto;font-size:14px}}
details{{background:var(--fon);border-radius:8px;padding:10px 14px;margin:8px 0}}
summary{{font-weight:700;cursor:pointer}}
footer{{text-align:center;color:var(--asosiy);font-size:13px;border-top:1px solid #e5e7eb;padding:16px}}
@media print{{
 header{{background:none;color:var(--asosiy);padding:0;margin:0 0 10px}}
 nav{{display:none}} details{{background:none;padding:0}} details>*{{display:block}}
 .qadam,.quti,table,details{{break-inside:avoid}} body{{font-size:11pt}}
}}"""
    sahifa = f"""<!doctype html>
<html lang="uz"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(SARLAVHA)} · Dars rejasi</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Montserrat:wght@700&display=swap" rel="stylesheet">
<style>{css}</style></head>
<body><main>{''.join(b)}</main><footer>{e(IMZO)}</footer>
<script>window.addEventListener('beforeprint',()=>document.querySelectorAll('details').forEach(d=>d.open=true))</script>
</body></html>"""
    with open(yol, "w", encoding="utf-8") as f:
        f.write(sahifa)


if __name__ == "__main__":
    fayllar = {
        "dars-rejasi.docx": dars_rejasi_docx,
        "topshiriq-varaqasi.docx": topshiriq_docx,
        "dars-rejasi.html": dars_rejasi_html,
    }
    for nom, fn in fayllar.items():
        yol = os.path.join(PAPKA, nom)
        fn(yol)
        print("Yaratildi:", yol)
