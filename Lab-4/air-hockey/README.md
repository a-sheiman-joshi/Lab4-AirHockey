# Air Hockey — Lab 4 completed implementation

## Features
- Circle-based puck/paddle collision response with overlap correction and angle-aware rebound.
- Scores for player and computer.
- 30-second countdown; match ends with a winner or draw.
- Puck is relaunched from the center after each goal.
- Arrow keys move the blue paddle; `R` restarts the match.

## Run on Ubuntu/Linux
```bash
cd air-hockey
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python main.py
```

If Pygame cannot open a window, make sure you are in a graphical desktop session.

## Controls
- Arrow keys: move the blue paddle (left half).
- R: restart match.
- Close window: quit.

## Lab submission reminders
Record a genuine 10-second video before making changes and another genuine 10-second video after all changes. Save both under your Lab repository's `Lab-4/` folder. Export the actual LLM conversation history/page link used during your work. Do not submit fabricated recordings or a reconstructed conversation as if it were the original chat.

## Screenshot evidence
If your instructor accepts screenshots instead of videos, capture the actual original game before editing as `before.png` and the finished game as `after.png`. Place both in your personal lab repository under `Lab-4/`. Make sure the after screenshot visibly shows the updated game; capture separate screenshots if one image cannot show all required features.
