# QR Code Generator

A lightweight and user-friendly desktop application for generating QR codes from text or URLs. Built with Python and Tkinter, it provides a clean and simple graphical interface to instantly create and save QR codes as PNG or JPEG images.

---

## Features

- **Simple & Intuitive UI** - Clean interface with a minimal design for quick QR code generation.
- **Text & URL Support** - Encode any text or URL into a QR code.
- **Save as PNG or JPEG** - Export generated QR codes in your preferred image format.
- **Cross-Platform** - Works on Windows, macOS, and Linux.

---

## Screenshots

> *Add a screenshot of the application here if desired.*

---

## Tech Stack

| Technology | Purpose           |
|------------|-------------------|
| Python 3   | Core language     |
| Tkinter    | GUI framework     |
| qrcode     | QR code generation|

---

## Prerequisites

- **Python 3.6+** installed on your system.
- The `qrcode` Python library.

---

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/QR-Code-Generator.git
   cd QR-Code-Generator
   ```

2. **Install the required dependency:**

   ```bash
   pip install qrcode[pil]
   ```

   > The `[pil]` extra installs the Pillow library, which is required for saving QR codes as images.

---

## Usage

1. **Run the application:**

   ```bash
   python qr_gen.py
   ```

2. **Generate a QR Code:**
   - Enter the text or URL you want to encode in the input field.
   - Click the **"Save QR-Code"** button.
   - Choose a save location and file format (PNG or JPEG).
   - A success message will confirm the file has been saved.

---

## Project Structure

```
QR-Code-Generator/
|-- qr_gen.py        # Main application script
|-- qr-code.ico      # Application icon
|-- README.md        # Project documentation
```

---

## How It Works

1. The application launches a Tkinter GUI window.
2. The user enters the desired text or URL into the input field.
3. Upon clicking **"Save QR-Code"**, a file dialog prompts the user to select a save location and image format.
4. The `qrcode` library generates the QR code from the input and saves it to the chosen path.
5. A confirmation message box is displayed with the saved file location.

---
