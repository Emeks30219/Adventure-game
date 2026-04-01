# 🗺️ Dead Road Adventure

A text-based adventure game built with Python where every choice leads to a different fate. Navigate through branching paths, meet strangers, and try to find your way out — alive.

---

## 📖 About

**Dead Road Adventure** is a CLI (Command Line Interface) story game written in Python. The player is placed at a dead end and must make a series of decisions that lead to either victory or defeat. With multiple branching paths and outcomes, no two playthroughs feel exactly the same.

This project was built as part of an ongoing Python learning journey, focusing on conditional logic, user input handling, and program flow.

---

## 🎮 How to Play

1. Run the script in your terminal or IDE
2. Enter your name when prompted
3. Read each scenario carefully and type your choice
4. Follow the story to its end — will you win or lose?

> **Tip:** Choices are not case-sensitive, so `LEFT`, `left`, and `Left` all work.

---

## 🌿 Story Paths

```
Start
├── Left
│   ├── Swim → 🐊 Eaten by crocodile (LOSE)
│   └── Walk → 💧 Run out of water (LOSE)
└── Right
    ├── Back → 🔙 Turn back (LOSE)
    └── Cross
        ├── Yes (talk to stranger) → 🏆 Get gold + directions (WIN!)
        └── No (ignore stranger)  → ❌ Wander the wrong way (LOSE)
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your machine

### Run the Game

```bash
python dead_road_adventure.py
```

---

## 📁 Project Structure

```
dead-road-adventure/
│
└── dead_road_adventure.py   # Main game script
```

---

## 🛠️ Built With

- **Python 3** — Core language
- **Built-in `input()`** — For interactive user prompts
- **Conditional logic (`if/elif/else`)** — For branching story paths

---

## 🧠 What I Learned

- Handling user input and normalising it with `.lower()`.
- Structuring nested `if/elif/else` blocks for branching logic.
- Designing a complete program flow with multiple outcomes.
- Writing clean, readable Python code.
