# Prompt Engineering 101

**Core idea:** The way you prompt an AI dramatically changes the quality of its output — from one generic answer to a structured comparison of solutions with tradeoff analysis.

---

## Example Problem

> *Find all duplicate first names in a class roster.*

---

## Three Solutions Compared

| Approach | Time | Space | Best when |
|---|---|---|---|
| Nested Loops | O(n²) | O(1) | Tiny lists, no imports |
| Sort + Scan | O(n log n) | O(1) | Memory-constrained |
| Hash Set | O(n) | O(n) | Most real-world cases |

---

## Files

| File | Purpose |
|---|---|
| `names.py` | Sample class roster (25 names, 3 duplicates) |
| `solutions.py` | Code examples for all three approaches with timing comparison |
| `demo_prompts.md` | Example prompts showing how prompt structure affects AI output |

---

## Running the Examples

```bash
python3 solutions.py
```
