# Live Demo Prompts

Use these prompts in order during the lesson. Paste them into Claude exactly as written.

---

## Step 1 — The Weak Prompt

> Write code to find duplicate names in a list.

**What to point out:** AI gives one solution. No tradeoffs, no alternatives, no complexity analysis. You got *an* answer, not *the best* answer.

---

## Step 2 — The Engineered Prompt

> I have a list of first names from a college class roster and I need to find any duplicate names.
> 
> Give me **3 different algorithmic approaches** — from the most naive to the most optimized.
> 
> For each approach:
> - Show the Python code
> - State the **time complexity** (Big-O)
> - State the **space complexity**
> - Explain in one sentence **when you'd use it**

**What to point out:** Same problem, much richer output. The prompt specified *breadth* (3 approaches), *structure* (4 things per approach), and *context* (college class roster → Python).

---

## Step 3 — The Follow-Up Prompt (Tradeoff Discussion)

> Now imagine this class has 1 million students instead of 25. Which approach would you recommend and why? Show me what happens to each algorithm's performance as n grows.

**What to point out:** Prompting AI to reason about *scale* is a real engineering skill. This mirrors how you'd actually evaluate solutions at work.

---

## Key Lesson

| Prompt quality | Output quality |
|---|---|
| Vague | One answer, no context |
| Structured | Multiple options + reasoning |
| Follow-up | Tradeoff analysis + scalability |

The skill is not "use AI." It's knowing how to **ask for breadth, then apply judgment.**
