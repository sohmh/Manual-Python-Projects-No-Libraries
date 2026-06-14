# Python Core Syntax Projects 🐍

> 15 projects, 5 tiers, zero libraries. Building real intuition for Python and the math, ML, and engineering it powers by writing everything from scratch.

This repository documents a structured, self-driven curriculum: **15 progressively harder projects built using *only* Python's core syntax and standard library.** No pandas, no numpy, no scikit-learn, no external dependencies of any kind  until the very last tier, where that absence becomes the whole point.

---

## Philosophy

The goal isn't to "finish Python." It's to build the kind of deep, load-bearing intuition that survives the moment I start using libraries  because by then, i'll already understand exactly what those libraries are doing for me and why they exist.

Each project is chosen to feed forward into real interests: motorsport/FSAE data analysis, quantitative finance, machine learning, and computational physics (CFD). The struggle of building things the hard way first is treated as a feature, not a bug , especially in Tier 5, where the projects are deliberately designed to make pure Python *hurt* just enough that reaching for a library afterward feels like a revelation rather than a shortcut.

---

## Ground Rules

1. **No Googling for syntax/concept doubts.** Work through them with Claude using the Socratic method (https://github.com/malkreide/socratic-method-skill) : guided questioning, not direct answers. The struggle is the crux of the learning.
2. **Finish a project before starting the next.** No jumping ahead.
3. **After "finishing" each project, add one unplanned feature.** This forces a return to the problem-solving mindset after the "core" implementation feels done.

---

## Repository Structure

```
python-core-projects/
├── tier-1-syntax-reinforcement/
│   ├── 01-cli-calculator-with-history/
│   ├── 02-word-frequency-analyzer/
│   └── 03-number-guessing-game/
├── tier-2-data-structures/
│   ├── 04-personal-finance-tracker/
│   ├── 05-flashcard-study-app/
│   └── 06-text-based-quiz-game/
├── tier-3-oop/
│   ├── 07-book-manager/
│   ├── 08-fsae-laptime-analyzer/
│   └── 09-expense-report-oop/
├── tier-4-algorithms/
│   ├── 10-sorting-algorithm-visualizer/
│   ├── 11-physics-simulator/
│   └── 12-linear-regression-from-scratch/
└── tier-5-bridge-projects/
    ├── 13-csv-data-analyzer/
    ├── 14-neural-network-from-scratch/
    └── 15-stock-return-calculator/
```

Each project folder contains its own source code, a short `notes.md` reflecting on what was learned, and the "extra feature" added after the core build was complete.

---

## The Roadmap

### Tier 1 — Syntax Reinforcement 
*Core toolkit: variables, loops, conditionals, functions, strings, lists, basic I/O*

#### Project 1: Command Line Calculator with History
A calculator that computes results, keeps a running history of every calculation in the session, and lets you recall previous results to use in new calculations.
- **Learn:** structuring functions properly, storing session data in lists, input validation (what if the user types "abc"?), infinite loops with clean exit conditions.
- **Why it matters:** input validation and error handling are critical in production ML code and financial applications.

#### Project 2: Word Frequency Analyzer
Reads text (pasted in, or from a `.txt` file), counts how often every word appears, strips common filler words ("the", "a", "is"), and shows the top 10 most frequent words.
- **Learn:** string methods, dictionaries as counters, sorting dictionaries by value, basic file reading.
- **Extension:** percentage frequency, sentence detection, average word length.
- **Why it matters:** text processing is the foundation of NLP — this is basic NLP without realizing it.

#### Project 3: Number Guessing Game with Statistics
The classic guessing game, extended to track stats across multiple rounds — average guesses per game, best game, worst game, win rate, and a leaderboard across multiple players.
- **Learn:** randomization (standard library), nested functions and game loops, basic statistics in pure Python, dictionaries for storing player data.
- **Why it matters:** building the stats system correctly is really a lesson in data structure design — a skill you'll use forever.

---

### Tier 2 — Data Structures Deep Dive 
*Builds on Tier 1 + heavy dictionary use, file I/O, more complex logic*

#### Project 4: Personal Finance Tracker
A CLI app to log income and expenses, categorize them (food, transport, education, entertainment), view summaries by category and monthly totals, and persist everything to a text/CSV file between sessions.
- **Learn:** file I/O (reading & writing), data persistence (your first taste of databases), dictionaries of lists (multiple transactions per category), string formatting for clean reports, basic `datetime` usage.
- **Why it matters:** you can eventually export your own portfolio data and analyze it with this tool — financial data pipelines in quant finance start exactly like this.

#### Project 5: Flashcard Study App
A terminal-based flashcard system (think Anki, but in the terminal). Add question/answer cards, study in a mode that lets you self-rate ("got it" / "needs review"), and prioritize the cards you get wrong more often.
- **Learn:** file I/O with structured data (your first semi-database), dictionaries with multiple fields per entry, basic spaced-repetition logic (weighting by performance), menus and navigation in CLI apps.
- **Why it matters:** this is a tool you'll actually use — for calculus formulas, physics laws, Python syntax. The best projects solve your own problems.

#### Project 6: Text-Based Quiz Game
A quiz game where questions and answers are loaded from a text file (not hardcoded). Supports multiple choice and true/false, tracks score and difficulty levels, and lets you add new questions through the program itself.
- **Learn:** separating data from logic (a huge software design principle), parsing structured text files, randomizing question order, timer functionality (`time` module).

---

### Tier 3 — Object-Oriented Programming 
*Builds on everything above + classes, objects, inheritance*

#### Project 7: Book Manager
A system to manage a personal book collection. Add books (title, author, year, genre, read/unread status), search by any field, mark as read, get recommendations by genre, and export your reading list.
- **Learn:** classes with multiple attributes and methods, lists of objects (not just lists of strings), searching through objects, file I/O with objects (serializing class instances).

#### Project 8: FSAE Lap-Time Analyzer
A simulation tool for analyzing racing lap data. Manually enter lap times, sector times, and track conditions; the program calculates average sector times, identifies the slowest sector, compares across different setup "configurations," and generates a text report.
- **Learn:** multiple interacting classes (`LapTime`, `Sector`, `Configuration`, `Session`), data aggregation across objects, generating formatted text reports, thinking about real engineering data.
- **Why it matters:** directly relevant to FSAE work — a way to contribute computationally to the team, and a natural bridge to pandas-based telemetry analysis later (imagine doing this on 10,000 laps).

#### Project 9: Expense Report Generator — OOP Version
Rebuild the Tier 2 finance tracker using proper OOP: `Transaction`, `Budget`, `Category`, and `Report` classes.
- **Learn:** why OOP exists — the contrast with the dictionary/list-based Tier 2 version makes the benefits immediately tangible.

---

### Tier 4 — Algorithms from Scratch 

#### Project 10: Sorting Algorithm Visualizer
Implement Bubble Sort, Selection Sort, Insertion Sort, Merge Sort, and Quick Sort from scratch. After each step, print the current state of the list as an ASCII bar chart so the sort is visible as it happens.
- **Learn:** algorithm implementation (thinking in discrete steps), recursion (merge sort & quick sort require it), time complexity intuition (watch bubble sort vs. quick sort on 50 elements), ASCII visualization logic.
- **Why it matters:** sorting algorithms come up in nearly every quant finance and ML engineering interview — understanding them from scratch is non-negotiable.

#### Project 11: Physics Simulator
Simulate projectile motion (a ball thrown at an angle) and print its ASCII trajectory. Input: initial velocity, angle, gravity. Output: full path, max height, range, and time of flight. Then extend it to simulate Venturi-effect pressure calculations for different tube geometries.
- **Learn:** translating physics equations into code, floating-point arithmetic and precision, iterative simulation (updating state each time step), the `math` module.
- **Why it matters:** computational physics *is* CFD — this is your first tiny CFD simulation.

#### Project 12: Linear Regression from Scratch
Implement linear regression using only Python's `math` module — no numpy, no scikit-learn. Given a list of (x, y) points, find the best-fit line and predict new values.

**Build in stages:**
1. Calculate mean, variance, and covariance manually (pure Python)
2. Implement the least-squares formula
3. Implement a gradient descent version
4. Compare both approaches on the same data
5. ASCII scatter plot with the best-fit line overlaid

- **Learn:** gradient descent — the most important ML algorithm, loss functions (mean squared error), iterative optimization, how ML actually works at its core.
- **Why it matters:** every ML algorithm you'll ever use is built on gradient descent. When numpy later does this in three lines, you'll know exactly what those lines mean.

---

### Tier 5 — Bridge Projects 
*These projects are designed to make you hit the wall of pure Python and naturally want libraries. That frustration is the point.*

#### Project 13: CSV Data Analyzer (without Pandas)
Read a real dataset (any CSV from Kaggle), parse it manually using Python's built-in `csv` module, and calculate mean, median, mode, standard deviation, min, and max for every numerical column. Filter rows by conditions and find correlations between columns.
- **Learn:** the `csv` module, implementing statistics from scratch, why data cleaning is hard (missing values, wrong types, encoding errors), nested list/dictionary manipulation at scale.
- **Why it matters:** by the end of this, you'll *desperately* want pandas — and when you start using it, you'll understand exactly what it's doing for you.

#### Project 14: Basic Neural Network from Scratch
Implement a simple 2-layer neural network using only Python lists and the `math` module. Train it on the classic XOR problem, implementing the forward pass, sigmoid activation, backpropagation, and weight updates.
- **Learn:** matrix operations with nested lists (painful without numpy), activation functions and why they exist, backpropagation conceptually, why numpy exists (you'll feel it in your soul).
- **Why it matters:** the math is heavy, but you already know the calculus — backprop *is* the chain rule. When you reimplement this with numpy, the difference will be profound.

#### Project 15: Stock/Mutual Fund Return Calculator
Fetch live stock/fund data using Python's `urllib` module (standard library, no `requests` needed — the unofficial Yahoo Finance API works well), calculate returns over custom time periods, compare multiple investments, calculate CAGR, and visualize with ASCII charts.
- **Learn:** HTTP requests with `urllib`, JSON parsing with the `json` module, API concepts in practice, financial calculations (CAGR, absolute and rolling returns).
- **Why it matters:** analyze your own portfolio. This is where the quant-finance interest meets practical Python — and becomes a real analysis tool once pandas and matplotlib are added later.

---

## Progress Tracker

- [ ] **Tier 1:** CLI Calculator · Word Frequency Analyzer · Number Guessing Game
- [ ] **Tier 2:** Personal Finance Tracker · Flashcard Study App · Text-Based Quiz Game
- [ ] **Tier 3:** Book Manager · FSAE Lap-Time Analyzer · Expense Report (OOP)
- [ ] **Tier 4:** Sorting Algorithm Visualizer · Physics Simulator · Linear Regression from Scratch
- [ ] **Tier 5:** CSV Data Analyzer · Neural Network from Scratch · Stock Return Calculator

---

## Requirements

- Python 3.x
- No external dependencies for Projects 1–14 (standard library only)
- Project 15 uses `urllib` and `json` from the standard library (no `requests`, `pandas`, etc.)

```bash
git clone <github.com/sohmh/Manual-Python-Projects-No-Libraries>
cd python-core-projects
python3 tier-1-syntax-reinforcement/01-cli-calculator-with-history/main.py
```

---

## 📜 License

MIT — feel free to use this curriculum structure for your own learning journey.
