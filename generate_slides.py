from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

# ── CodePath palette ───────────────────────────────────────────────────────────
CP_GREEN   = RGBColor(0x33, 0xC3, 0x85)  # codepath.org primary
CP_DARK    = RGBColor(0x0D, 0x0D, 0x0D)  # near-black background
CP_CARD    = RGBColor(0x1A, 0x1A, 0x1A)  # card / code block background
CP_BORDER  = RGBColor(0x2E, 0x2E, 0x2E)  # subtle border
WHITE      = RGBColor(0xFF, 0xFF, 0xFF)
GRAY       = RGBColor(0x99, 0x99, 0x99)
RED        = RGBColor(0xFF, 0x4D, 0x4D)  # wrong-answer indicator

prs = Presentation()
prs.slide_width  = Inches(13.33)
prs.slide_height = Inches(7.5)
BLANK = prs.slide_layouts[6]


def bg(slide, color=CP_DARK):
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = color


def box(slide, left, top, width, height, fill_color=CP_CARD, border_color=CP_BORDER, border_pt=1):
    s = slide.shapes.add_shape(1, Inches(left), Inches(top), Inches(width), Inches(height))
    s.fill.solid()
    s.fill.fore_color.rgb = fill_color
    s.line.color.rgb = border_color
    s.line.width = Pt(border_pt)
    return s


def txt(slide, text, left, top, width, height,
        size=20, bold=False, italic=False, color=WHITE, align=PP_ALIGN.LEFT):
    txb = slide.shapes.add_textbox(Inches(left), Inches(top), Inches(width), Inches(height))
    txb.word_wrap = True
    tf = txb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = color
    return txb


def green_bar(slide):
    b = slide.shapes.add_shape(1, Inches(0), Inches(0), Inches(13.33), Inches(0.1))
    b.fill.solid()
    b.fill.fore_color.rgb = CP_GREEN
    b.line.fill.background()


def label(slide, text, left, top):
    txt(slide, text, left, top, 4, 0.3, size=11, bold=True, color=CP_GREEN)


# ── SLIDE 1: Title ─────────────────────────────────────────────────────────────
s1 = prs.slides.add_slide(BLANK)
bg(s1)
green_bar(s1)

# green accent left bar
b = s1.shapes.add_shape(1, Inches(0.55), Inches(2.4), Inches(0.08), Inches(2.0))
b.fill.solid()
b.fill.fore_color.rgb = CP_GREEN
b.line.fill.background()

txt(s1, "Prompt Engineering 101", 0.8, 2.4, 12, 1.1, size=54, bold=True)
txt(s1, "How the way you ask changes everything", 0.8, 3.6, 10, 0.6,
    size=22, italic=True, color=GRAY)
txt(s1, "codepath.org", 0.8, 6.9, 4, 0.4, size=13, color=CP_GREEN)


# ── SLIDE 2: Check for Understanding (funny + tricky) ─────────────────────────
s2 = prs.slides.add_slide(BLANK)
bg(s2)
green_bar(s2)

txt(s2, "Which prompt gets the best result?", 0.5, 0.25, 12, 0.65, size=30, bold=True)
txt(s2, "You need to find duplicate first names in a class roster. Choose wisely. 👀",
    0.5, 0.95, 12.3, 0.45, size=16, color=GRAY, italic=True)

choices = [
    ("A", '"write code to find duplicates"',
     False, '← too vague'),
    ("B", '"As a world-class algorithm genius with 200 IQ, craft me the most\n     magnificent, flawless, perfect solution ever written ✨"',
     False, '← flattery ≠ clarity  🤡'),
    ("C", '"Give me 3 Python solutions to find duplicate first names — include\n     time complexity, space complexity, and when to use each."',
     True,  '← structured = better output ✓'),
    ("D", '"pls help im crying 😭  duplicates... names... list... python... help"',
     False, '← we\'ve all been here'),
]

tops = [1.65, 2.55, 3.7, 4.85]
for (letter, text, correct, note), top in zip(choices, tops):
    h = 0.75 if letter != "B" else 0.85
    border_col = CP_GREEN if correct else CP_BORDER
    fill_col   = RGBColor(0x0C, 0x2B, 0x1F) if correct else CP_CARD
    box(s2, 0.4, top, 12.5, h, fill_color=fill_col, border_color=border_col,
        border_pt=2 if correct else 1)
    text_col = CP_GREEN if correct else (GRAY if letter in ("A","D") else WHITE)
    txt(s2, f"  {letter})  {text}", 0.5, top + 0.07, 9.5, h, size=16, color=text_col)
    note_col = CP_GREEN if correct else RED if letter == "B" else GRAY
    txt(s2, note, 10.1, top + 0.2, 2.7, 0.4, size=12, italic=True, color=note_col,
        align=PP_ALIGN.RIGHT)


# ── SLIDE 3: Lazy vs Structured ────────────────────────────────────────────────
s3 = prs.slides.add_slide(BLANK)
bg(s3)
green_bar(s3)

txt(s3, "Lazy Prompt vs. Structured Prompt", 0.5, 0.2, 12, 0.6, size=28, bold=True)

# Left — lazy
label(s3, "LAZY", 0.5, 0.95)
box(s3, 0.5, 1.3, 5.9, 0.65, border_color=RED)
txt(s3, '"Write code to find duplicate names."', 0.65, 1.37, 5.6, 0.5,
    size=14, italic=True, color=GRAY)

label(s3, "WHAT YOU GET", 0.5, 2.1)
box(s3, 0.5, 2.45, 5.9, 2.7)
txt(s3,
    "def find_duplicates(names):\n"
    "    result = []\n"
    "    for i in range(len(names)):\n"
    "        for j in range(i+1, len(names)):\n"
    "            if names[i] == names[j]:\n"
    "                result.append(names[i])\n"
    "    return result\n\n"
    "# One solution. No explanation. Good luck.",
    0.65, 2.52, 5.6, 2.55, size=12, color=GRAY)

# Right — structured
label(s3, "STRUCTURED", 7.0, 0.95)
box(s3, 7.0, 1.3, 5.9, 0.65, border_color=CP_GREEN)
txt(s3, '"Give me 3 Python solutions... time complexity,\n space complexity, when to use each."',
    7.15, 1.37, 5.6, 0.5, size=14, italic=True, color=WHITE)

label(s3, "WHAT YOU GET", 7.0, 2.1)
rows = [
    ("Nested Loops",  "O(n²)",      "O(1)"),
    ("Sort + Scan",   "O(n log n)", "O(1)"),
    ("Hash Set",      "O(n)",       "O(n)"),
]
box(s3, 7.0, 2.45, 5.9, 2.7, border_color=CP_GREEN)
headers = ["Approach", "Time", "Space"]
hx = [7.15, 9.7, 11.4]
for h, x in zip(headers, hx):
    txt(s3, h, x, 2.55, 2.0, 0.35, size=12, bold=True, color=CP_GREEN)
for r_i, (approach, time, space) in enumerate(rows):
    y = 3.05 + r_i * 0.65
    txt(s3, approach, 7.15, y, 2.4, 0.5, size=14)
    txt(s3, time,     9.7,  y, 1.6, 0.5, size=14, color=GRAY)
    txt(s3, space,   11.4,  y, 1.4, 0.5, size=14, color=GRAY)

txt(s3, "Same question. One prompt gives you options + reasoning.",
    0.5, 5.3, 12.3, 0.5, size=15, italic=True, color=GRAY, align=PP_ALIGN.CENTER)


# ── SLIDE 4: Advanced Prompt ───────────────────────────────────────────────────
s4 = prs.slides.add_slide(BLANK)
bg(s4)
green_bar(s4)

txt(s4, "Level Up: The Advanced Prompt", 0.5, 0.2, 12, 0.6, size=28, bold=True)
txt(s4, "Add scale + constraints → get a recommendation, not just code",
    0.5, 0.85, 12, 0.45, size=16, italic=True, color=GRAY)

label(s4, "PROMPT", 0.5, 1.45)
box(s4, 0.5, 1.8, 12.3, 1.35, border_color=CP_GREEN)
txt(s4,
    "Now imagine this class has 1,000,000 students instead of 25.\n"
    "Which approach do you recommend and why? Show how each algorithm scales as n grows.\n"
    "Are there any edge cases I should handle?",
    0.65, 1.87, 12.0, 1.2, size=15, italic=True)

label(s4, "WHAT YOU GET", 0.5, 3.3)
gains = [
    ("✓", "Clear recommendation with justification (Hash Set wins at scale)"),
    ("✓", "Performance comparison: O(n²) is 40,000× slower at n=1M vs O(n)"),
    ("✓", "Edge cases surfaced: empty list, case sensitivity, all-duplicate lists"),
    ("✓", "Real constraints: memory trade-off explained for embedded/low-RAM systems"),
]
for i, (icon, g) in enumerate(gains):
    y = 3.65 + i * 0.62
    txt(s4, icon, 0.5, y, 0.4, 0.5, size=18, bold=True, color=CP_GREEN)
    txt(s4, g,    0.95, y, 11.8, 0.5, size=16)


# ── SLIDE 5: Takeaway ──────────────────────────────────────────────────────────
s5 = prs.slides.add_slide(BLANK)
bg(s5)
green_bar(s5)

txt(s5, "The Takeaway", 0.5, 0.3, 12, 0.6, size=32, bold=True)

cards = [
    ("Vague prompt",      "One answer.\nNo tradeoffs.",          False),
    ("Structured prompt", "Multiple options.\nWith reasoning.",  True),
    ("Follow-up prompt",  "Scale analysis.\nEdge cases.",        True),
]
for i, (title, body, highlight) in enumerate(cards):
    x = 0.55 + i * 4.25
    border = CP_GREEN if highlight else CP_BORDER
    fill   = RGBColor(0x0C, 0x2B, 0x1F) if highlight else CP_CARD
    box(s5, x, 1.2, 3.9, 2.5, fill_color=fill, border_color=border, border_pt=2 if highlight else 1)
    col = CP_GREEN if highlight else GRAY
    txt(s5, title, x + 0.15, 1.4,  3.6, 0.5, size=16, bold=True, color=col)
    txt(s5, body,  x + 0.15, 2.0,  3.6, 1.5, size=22, bold=True)

txt(s5, "Prompt engineering isn't about magic words.", 0.5, 4.1, 12.3, 0.5,
    size=22, bold=True, align=PP_ALIGN.CENTER)
txt(s5, "It's about asking for breadth, then applying your own judgment.",
    0.5, 4.65, 12.3, 0.5, size=18, italic=True, color=GRAY, align=PP_ALIGN.CENTER)

b2 = s5.shapes.add_shape(1, Inches(4.5), Inches(5.35), Inches(4.33), Inches(0.06))
b2.fill.solid()
b2.fill.fore_color.rgb = CP_GREEN
b2.line.fill.background()

txt(s5, "codepath.org", 5.6, 5.55, 2.5, 0.4, size=14, bold=True, color=CP_GREEN,
    align=PP_ALIGN.CENTER)


# ── Save ───────────────────────────────────────────────────────────────────────
prs.save("slides.pptx")
print("slides.pptx created — import into Google Slides via File → Import slides")
