# Prompt Engineering 101

## Files

| File | Purpose |
|---|---|
| `names.py` | Sample class roster (25 names, 3 duplicates) |
| `solutions.py` | Code examples for all three approaches with timing comparison |
| `demo_prompts.md` | Example prompts showing how prompt structure affects AI output |
| `generate_slides.py` | Generates `slides.pptx` for import into Google Slides |

---

## Running the Examples

```bash
python3 solutions.py
```

## Generating Slides

```bash
python3 -m venv venv
source venv/bin/activate
pip install python-pptx
python3 generate_slides.py
```

Then open [Google Slides](https://slides.google.com) → File → Import slides → upload `slides.pptx`.
