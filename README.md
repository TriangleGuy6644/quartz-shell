# Quartz Shell 🪞🧠

Quartz Shell is a modular Python-based command shell with support for plug-in-like utilities ("gems") such as calculators, image tools, and system utilities. It features themes, command autocompletion, and a customizable prompt.

---

## 🔧 Features

- 🧱 Modular command system ("gems")
- 🎨 Theme support with ANSI color customization
- 🧠 Smart autocompletion using `prompt_toolkit`
- 🖼️ Tools like image editors, calculators, and more
- 🗃️ Configurable prompt prefix and shell behavior
- 📦 Easily installable and extendable utility structure

---

## 📁 Project Structure

```
quartz-shell/
├── assets/           # Banners and visual assets
├── config/           # User configuration files (e.g. config.json)
├── gems/             # Individual tools (calculator, image editor, etc.)
│   └── image.py
├── shell/            # Core shell logic
│   ├── core.py       # Main shell loop
│   ├── commands.py   # Optional command dispatcher
│   └── themes.py     # Theme definitions and helpers
├── main.py           # Entry point for launching the shell
└── README.md
```

---

## 🚀 Getting Started

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the shell

```bash
python -m quartz.py
```

---

## 💎 Creating Gems

Add a new Python file to the `gems/` folder. Example structure:

```python
def main(args):
    print("This is your new gem!")
```

The filename becomes the command: `gemname.py` → `> gemname`.

---

## 🎨 Themes

Themes are defined in `shell/themes.py`. You can switch the active theme using:

```
> theme set [theme_name]
```

View all available themes:

```
> theme list
```

---

## ⚙️ Configuration

User settings like theme and prompt prefix are stored in `config/config.json`. This file is auto-generated on first run.

---

## 📄 .gitignore

```
config/config.json
__pycache__/
```

---

## 🧠 Dependencies

- [`prompt_toolkit`](https://github.com/prompt-toolkit/python-prompt-toolkit)
- Standard Python libraries (`os`, `json`, `importlib`, etc.)

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. **Fork** the repository
2. **Clone** your fork:
   ```bash
   git clone https://github.com/yourusername/quartz-shell.git
   ```
3. **Create a branch** for your feature or fix:
   ```bash
   git checkout -b my-new-feature
   ```
4. **Make your changes**
5. **Commit** with a descriptive message:
   ```bash
   git commit -am "Add feature X"
   ```
6. **Push** to your fork:
   ```bash
   git push origin my-new-feature
   ```
7. **Open a Pull Request** on GitHub

Please follow consistent code style and structure. Tests and doc updates are appreciated!

---

## 🪲 TODO

- [ ] Add support for installing gems dynamically
- [ ] Package as a Python module
- [ ] Add better error output for invalid commands
- [ ] Write unit tests

---

## 📜 License

MIT License.
