
# 🔐 Password Strength Analyzer with Custom Wordlist Generator

## 🧠 Overview

This project is a Python-based tool that allows users to:
- Analyze the strength of passwords using the `zxcvbn` library.
- Generate custom wordlists based on user-provided personal information.
- Export wordlists in `.txt` format for use in security testing tools.
- Interact through both Command-Line Interface (CLI) and a GUI (Tkinter).

## 🚀 Features

- Password strength analysis using entropy and pattern detection.
- Custom wordlist generation using names, years, pet names, etc.
- Includes leetspeak and common password mutation patterns.
- GUI interface built with Tkinter.
- Exports `.txt` files for penetration testing purposes.

## 🛠️ Tools & Libraries Used

- Python 3.x
- [zxcvbn](https://github.com/dropbox/zxcvbn)
- nltk
- tkinter (standard Python library)
- argparse

## 📦 Installation

Make sure Python is installed and added to PATH.

Install dependencies:

```bash
pip install zxcvbn nltk tqdm
```

## 💡 How to Run

### ▶️ Command Line Version

```bash
python password_tool.py
```

Follow the CLI prompts to analyze a password or generate a wordlist.

### 🖼️ GUI Version

```bash
python password_tool_gui.py
```

A window will appear where you can enter password data and generate wordlists.

## 📂 Project Structure

```
├── password_tool.py             # CLI script
├── password_tool_gui.py         # GUI version
├── wordlist.txt                 # Sample output wordlist
├── Password_Strength_Analyzer_Report.docx  # Project report
├── README.md                    # Project documentation
└── requirements.txt             # List of dependencies
```

## 📄 Sample Wordlist Output

```
tiku123
$nayanatiku
NAYANA2003
nayana2003!
#nayana
...
```

## ✅ Deliverables

- ✅ CLI tool for password analysis
- ✅ GUI with tkinter
- ✅ Wordlist generator
- ✅ Export to .txt format
- ✅ Project Report (.docx)

## 👨‍💻 Author
nayanadaskk369@gmail.com  
Created as part of a cybersecurity learning project. Feel free to fork or contribute!

---

> ⚠️ For educational use only. Do not use against systems you do not own or have permission to test.
