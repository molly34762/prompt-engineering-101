# Prompt Engineering 101

A 10–15 minute lesson demo on **Algorithmic Thinking + Prompt Engineering** for undergraduate students.

**Core idea:** The way you prompt an AI dramatically changes the quality of its output — from one generic answer to a structured comparison of solutions with tradeoff analysis.

---

## The Problem

> *Find all duplicate first names in a class roster.*

Simple enough for any student to understand. Rich enough to have three meaningfully different algorithmic solutions.

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
| `solutions.py` | All three approaches with timing comparison |
| `demo_prompts.md` | Exact prompts to paste into Claude during the live demo |

---

## Running the Demo

```bash
python solutions.py
```

---

## Lesson Flow

1. **Weak prompt** — show how a vague ask produces one answer with no tradeoffs
2. **Engineered prompt** — structured ask produces 3 solutions with complexity analysis
3. **Follow-up prompt** — ask AI to reason about scale (what if n = 1,000,000?)
4. **Key takeaway** — prompt engineering is about asking for breadth, then applying judgment

See [`demo_prompts.md`](demo_prompts.md) for the exact prompts used in each step.
