# Software Engineering Lab Submissions

**Student:** A Sheiman Joshi  
**SRN:** PES2UG24CS003  

---

## Lab 5 — Static Code Analysis (Retail POS & Discount Tracker)

**Folder:** [`Lab-5/`](./Lab-5/)  
**Original Repo:** https://github.com/SETAPESU26/L5_02_retail_pos  

### Lab-5 Deliverables
- [`pos_system.py`](./Lab-5/pos_system.py) — Cleaned POS script (Pylint: **10.00/10**, Bandit: **0 issues**, Flake8: **0 errors**)
- [`issues.md`](./Lab-5/issues.md) — Comprehensive issues table (High/Medium severity first)
- [`reflection.md`](./Lab-5/reflection.md) — Answers to the 4 reflection questions
- [`pos_system_original.py`](./Lab-5/pos_system_original.py) — Original script before refactoring
- Analysis Reports: [`pylint_report.txt`](./Lab-5/pylint_report.txt), [`bandit_report.txt`](./Lab-5/bandit_report.txt), [`flake8_report.txt`](./Lab-5/flake8_report.txt)

---

## Lab 4 — Vibe Coding (Air Hockey)

**Folder:** [`Lab-4/`](./Lab-4/)  
**Original Repo:** https://github.com/SETAPESU26/02_air_hockey  

### Lab-4 Contents
- `before.png` — Screenshot of original broken game
- `after.png` — Screenshot of completed game with scoring, timer, and collision fixes
- `chat_history.pdf` — Exported AI pair-programming conversation
- `air-hockey/` — Updated source code with all four tasks completed

### Tasks Completed
1. **Fixed puck–paddle collision** — Circle-circle geometry with overlap separation and normal reflection
2. **Implemented match scoring** — Goal detection within goal openings, wall bounces elsewhere
3. **Added 30-second match timer** — Monotonic-clock countdown, game-over with winner/draw
4. **Puck reset after scoring** — Center relaunch with directional velocity

### How to Run Lab 4
```bash
cd Lab-4/air-hockey
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```
