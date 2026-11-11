# gdg-calculator-app
Calculator ~ [Tkinter Edition] made in python as gdg app development project task

# Calculator ~ [Tkinter Edition] 🧮

A lightweight, customizable desktop calculator built with Python and Tkinter for the **GDG App Development Round 2** selection task.

## ✨ Features
- **Core & Scientific Operations:** Supports Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), Exponents (`^`), Percentage (`%`), Parentheses `()`, and Pi (`π`).
- **Centralized Theme Engine (Light & Dark Mode):** Uses top-level theme dictionaries (similar to CSS stylesheets) to dynamically switch UI colors and hover states across all widgets with one click.
- **Custom Button Subclass:** Inherits from `tk.Button` to manage global instance tracking, custom `<Enter>`/`<Leave>` hover events, and instant theme updates.
- **Quick Editing Controls:** Includes both full clear (`C`) and single-character backspace (`del`).

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **GUI Framework:** Tkinter (Standard Library)
- **Math Module:** Python `math` library

## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/Mukul-Koli/gdg-calculator-app.git
   ```
2. Navigate into the project directory:
   ```bash
   cd gdg-calculator-app
   ```
3. Run the application:
   ```bash
   python calculator.py
   ```

## 🧠 Architecture Highlights
- **Decoupled Styling:** UI configurations (`modes_screen_cfg` and `modes_btnframe_cfg`) are defined separately at the top of the script so colors and fonts can be modified without touching calculation logic.
- **Safe Expression Evaluation:** Translates user-friendly symbols (`^`, `%`, `π`) into valid Python expressions before evaluating inside a `try-except` error handler.
