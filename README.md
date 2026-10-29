# Lab 4 — Vibe Coding (Air Hockey)

**Student:** A Sheiman Joshi  
**SRN:** PES2UG24CS003  
**Original Repo:** https://github.com/SETAPESU26/02_air_hockey

## Lab-4 Contents

- `before.png` — Screenshot of original broken game
- `after.png` — Screenshot of completed game with scoring, timer, and collision fixes
- `chat_history.pdf` — Exported AI pair-programming conversation
- `air-hockey/` — Updated source code with all four tasks completed

## Tasks Completed

1. **Fixed puck–paddle collision** — Circle-circle geometry with overlap separation and normal reflection
2. **Implemented match scoring** — Goal detection within goal openings, wall bounces elsewhere
3. **Added 30-second match timer** — Monotonic-clock countdown, game-over with winner/draw
4. **Puck reset after scoring** — Center relaunch with directional velocity

## How to Run

```bash
cd Lab-4/air-hockey
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

**Controls:** Arrow keys to move paddle, R to restart.
