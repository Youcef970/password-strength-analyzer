# 🔐 Password Strength Analyzer Pro

A professional password strength checker with entropy calculation, real-time breach detection, and a modern user interface.

## 🎯 Features

- **Real-time password strength analysis** - Updates as you type
- **Entropy calculation** - Information theory-based strength measurement
- **Breach detection** - Checks against 10B+ leaked passwords via HIBP API (k-Anonymity)
- **Password generator** - Cryptographically secure random passwords
- **Clipboard safety** - Auto-clears clipboard after 15 seconds
- **Crack time estimation** - How long to brute force
- **Modern GUI** - Dark mode, professional design

## 🛠️ Tech Stack

- Python 3.8+
- CustomTkinter / Tkinter (modern GUI)
- Requests (API calls)
- HIBP API (breach checking)

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/password-strength-analyzer.git

# Navigate to project
cd password-strength-analyzer

# Install dependencies
pip install requests customtkinter

# Run the application
python main.py
