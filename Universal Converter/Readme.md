# 🧠 UNIVERSAL CONVERTER

A modern Python-based desktop application to convert data between multiple formats including **Text**, **Binary**, **Decimal**, and **Hexadecimal**. Built with modular Python logic and a responsive **PyQt5 GUI**.

---

## 🚀 Features

- 🔄 Convert between:
  - Text ⇄ Binary
  - Text ⇄ Decimal
  - Text ⇄ Hex
  - Binary ⇄ Decimal
  - Binary ⇄ Hex
  - Decimal ⇄ Hex
- ✅ Clean and centered GUI layout using PyQt5
- ⌨️ Real-time manual input
- ✨ Responsive interface with styled buttons and fields
- 💡 Modular architecture (separate files for conversion logic)

---

## 🖼️ GUI Preview

![Universal Converter GUI](gui_screenshot.png)

---

## 📂 Project Structure
```
converter/
├── gui.py                    # PyQt5 GUI
├── main.py                   # Logic controller
├── text_conversions.py       # Text <-> Binary/Decimal/Hex functions
├── binary_conversions.py     # Binary <-> Text/Decimal/Hex functions
├── decimal_conversions.py    # Decimal <-> Text/Binary/Hex functions
├── hex_conversions.py        # Hex <-> Text/Binary/Decimal functions
```


---

## 🛠️ Installation

### 1. Clone the Repository

```
git clone https://github.com/your-username/universal-converter.git
cd universal-converter
```

### 2. Install Dependencies
```
pip install PyQt5
```

### 3. Run the App
```
python gui.py

```

### 4. Example Conversion
