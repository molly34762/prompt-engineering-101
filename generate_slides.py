from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

# ── Color palette ──────────────────────────────────────────────────────────────
BLACK      = RGBColor(0x1A, 0x1A, 0x2E)   # dark navy — backgrounds
ACCENT     = RGBColor(0xE9, 0x4F, 0x37)   # red-orange — highlights
WHITE      = RGBColor(0xFF, 0xFF, 0xFF)
LIGHT_GRAY = RGBColor(0xF2, 0xF2, 0xF2)
MID_GRAY   = RGBColor(0xCC, 0xCC, 0xCC)
CODE_BG    = RGBColor(0x2B, 0x2D, 0x42)   # dark code block

prs = Presentation()
prs.slide_width  = Inches(13.33)
prs.slide_height = Inches(7.5)

BLANK = prs.slide_layouts[6]  # fully blank layout


def bg(slide, color=BLACK):
    """Fill slide background with a solid color."""
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = color


def add_text(slide, text, left, top, width, height,
             size=24, bold=False, color=WHITE, align=PP_ALIGN.LEFT, italic=False):
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


def add_code_block(slide, code, left, top, width, height, size=13):
    """Dark box with monospace code text."""
    shape = slide.shapes.add_shape(
        1,  # MSO_SHAPE_TYPE.RECTANGLE
        Inches(left), Inches(top), Inches(width), Inches(height)
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = CODE_BG
    shape.line.color.rgb = ACCENT
    shape.line.width = Pt(1.5)

    tf = shape.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    run = p.add_run()
    run.text = code
    run.font.size = Pt(size)
    run.font.color.rgb = WHITE
    run.font.name = "Courier New"
    return shape


def accent_bar(slide):
    """Thin colored bar at the top of the slide."""
    bar = slide.shapes.add_shape(1, Inches(0), Inches(0), Inches(13.33), Inches(0.12))
    bar.fill.solid()
    bar.fill.fore_color.rgb = ACCENT
    bar.line.fill.background()


# ── SLIDE 1: Title ─────────────────────────────────────────────────────────────
s1 = prs.slides.add_slide(BLANK)
bg(s1)
accent_bar(s1)
add_text(s1, "Prompt Engineering 101", 1, 2.2, 11, 1.2, size=52, bold=True, align=PP_ALIGN.CENTER)
add_text(s1, "How the way you ask changes everything", 1, 3.6, 11, 0.8, size=24, color=MID_GRAY, align=PP_ALIGN.CENTER, italic=True)


# ── SLIDE 2: Check for Understanding ──────────────────────────────────────────
s2 = prs.slides.add_slide(BLANK)
bg(s2)
accent_bar(s2)
add_text(s2, "Quick Check", 0.5, 0.25, 12, 0.5, size=14, color=ACCENT, bold=True)
add_text(s2, "Which prompt will get you the best result?", 0.5, 0.8, 12, 0.9, size=32, bold=True)
add_text(s2, "You need to find duplicate names in a list of students.", 0.5, 1.75, 12, 0.5, size=18, color=MID_GRAY)

choices = [
    ('A', '"Write code to find duplicates"'),
    ('B', '"Give me 3 Python solutions to find duplicate first names, with time\n     complexity and when to use each"'),
    ('C', '"Help me with duplicates please"'),
    ('D', '"code duplicates python list"'),
]
tops = [2.5, 3.4, 4.5, 5.4]
for (letter, text), top in zip(choices, tops):
    # highlight box for B
    if letter == 'B':
        box = s2.shapes.add_shape(1, Inches(0.4), Inches(top - 0.1), Inches(12.4), Inches(0.75))
        box.fill.solid()
        box.fill.fore_color.rgb = RGBColor(0x2A, 0x0A, 0x08)
        box.line.color.rgb = ACCENT
        box.line.width = Pt(1.5)
    add_text(s2, f"{letter})  {text}", 0.6, top, 12, 0.8, size=19,
             color=ACCENT if letter == 'B' else WHITE)


# ── SLIDE 3: The Lazy Prompt ───────────────────────────────────────────────────
s3 = prs.slides.add_slide(BLANK)
bg(s3)
accent_bar(s3)
add_text(s3, "The Lazy Prompt", 0.5, 0.25, 8, 0.5, size=14, color=ACCENT, bold=True)
add_text(s3, "Vague ask → one answer, no tradeoffs", 0.5, 0.75, 9, 0.6, size=30, bold=True)

add_text(s3, "PROMPT", 0.5, 1.6, 3, 0.35, size=12, color=MID_GRAY, bold=True)
add_code_block(s3, '"Write code to find duplicate names in a list."', 0.5, 2.0, 12.3, 0.7, size=18)

add_text(s3, "WHAT YOU GET", 0.5, 2.95, 4, 0.35, size=12, color=MID_GRAY, bold=True)
add_code_block(
    s3,
    "def find_duplicates(names):\n"
    "    duplicates = []\n"
    "    for i in range(len(names)):\n"
    "        for j in range(i + 1, len(names)):\n"
    "            if names[i] == names[j] and names[i] not in duplicates:\n"
    "                duplicates.append(names[i])\n"
    "    return duplicates",
    0.5, 3.35, 6.5, 2.9, size=13
)

add_text(s3, "What's missing?", 7.3, 3.35, 5.5, 0.45, size=16, bold=True, color=ACCENT)
problems = ["✗  Only one solution", "✗  No time complexity", "✗  No space complexity", "✗  No alternatives", "✗  No guidance on when to use it"]
for i, p in enumerate(problems):
    add_text(s3, p, 7.3, 3.9 + i * 0.52, 5.5, 0.5, size=16, color=MID_GRAY)


# ── SLIDE 4: The Structured Prompt ────────────────────────────────────────────
s4 = prs.slides.add_slide(BLANK)
bg(s4)
accent_bar(s4)
add_text(s4, "The Structured Prompt", 0.5, 0.25, 10, 0.5, size=14, color=ACCENT, bold=True)
add_text(s4, "Tell AI what you need — breadth + format", 0.5, 0.75, 11, 0.6, size=30, bold=True)

add_text(s4, "PROMPT", 0.5, 1.6, 3, 0.35, size=12, color=MID_GRAY, bold=True)
add_code_block(
    s4,
    "I have a list of first names from a college class roster and need to find duplicates.\n"
    "Give me 3 different algorithmic approaches — from naive to optimized.\n"
    "For each: show the Python code, state the time complexity, state the space complexity,\n"
    "and explain in one sentence when you'd use it.",
    0.5, 2.0, 12.3, 1.3, size=14
)

add_text(s4, "WHAT YOU GET", 0.5, 3.5, 4, 0.35, size=12, color=MID_GRAY, bold=True)

headers = ["Approach", "Time", "Space", "Use when"]
col_x   = [0.5, 5.2, 7.2, 9.0]
col_w   = [4.5, 1.8, 1.6, 4.1]
rows = [
    ["Nested Loops",  "O(n²)",      "O(1)",  "Tiny lists"],
    ["Sort + Scan",   "O(n log n)", "O(1)",  "Memory-constrained"],
    ["Hash Set",      "O(n)",       "O(n)",  "Most real-world cases"],
]
# header row
for hdr, x, w in zip(headers, col_x, col_w):
    add_text(s4, hdr, x, 3.9, w, 0.4, size=13, bold=True, color=ACCENT)

for r_i, row in enumerate(rows):
    for val, x, w in zip(row, col_x, col_w):
        add_text(s4, val, x, 4.4 + r_i * 0.55, w, 0.5, size=14,
                 color=ACCENT if val == "O(n)" else WHITE)


# ── SLIDE 5: The Advanced Prompt ──────────────────────────────────────────────
s5 = prs.slides.add_slide(BLANK)
bg(s5)
accent_bar(s5)
add_text(s5, "The Advanced Prompt", 0.5, 0.25, 10, 0.5, size=14, color=ACCENT, bold=True)
add_text(s5, "Add scale + constraints → get a recommendation", 0.5, 0.75, 12, 0.6, size=30, bold=True)

add_text(s5, "PROMPT", 0.5, 1.6, 3, 0.35, size=12, color=MID_GRAY, bold=True)
add_code_block(
    s5,
    "Now imagine this class has 1,000,000 students instead of 25.\n"
    "Which of the 3 approaches would you recommend and why?\n"
    "Show how each algorithm's performance changes as n grows.\n"
    "Are there any edge cases I should handle?",
    0.5, 2.0, 12.3, 1.3, size=14
)

add_text(s5, "WHAT YOU GET", 0.5, 3.5, 4, 0.35, size=12, color=MID_GRAY, bold=True)
gains = [
    "✓  Clear recommendation with justification",
    "✓  Growth curve comparison across all 3 approaches",
    "✓  Edge cases: empty list, all duplicates, case sensitivity",
    "✓  Real-world constraints surfaced (memory, data size)",
]
for i, g in enumerate(gains):
    add_text(s5, g, 0.5, 4.0 + i * 0.62, 12.3, 0.55, size=18,
             color=ACCENT if g.startswith("✓") else WHITE)

add_text(s5, "Prompt engineering = asking for breadth, then applying judgment.",
         0.5, 6.6, 12.3, 0.6, size=16, italic=True, color=MID_GRAY, align=PP_ALIGN.CENTER)


# ── Save ──────────────────────────────────────────────────────────────────────
prs.save("slides.pptx")
print("slides.pptx created — import into Google Slides via File → Import slides")
