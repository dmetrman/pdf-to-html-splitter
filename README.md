# PDF Processing Toolkit

This repository provides Python scripts for splitting PDF files into smaller parts and converting PDFs to HTML using `pdf2htmlEX`.

## Features
- **PDF Splitting**: Extract specific page ranges from a PDF and save them as separate files.
- **PDF to HTML Conversion**: Convert PDFs to HTML format using `pdf2htmlEX`.

---

## Installation

### 1️⃣ Install Python & Dependencies
Make sure you have Python installed.

Install required dependencies using:
```sh
pip install -r requirements.txt
```

---

## Usage

### 2️⃣ Splitting a PDF
To split a PDF into parts based on specific page ranges, use `split_pdf.py`.

#### Example
```sh
python split_pdf.py
```

By default, the script will split `new_file.pdf` into three parts:
- Pages 1-5
- Pages 5-10
- Pages 10-15

You can modify `input_pdf`, `output_folder`, `output_prefix`, and `ranges` in the script.

---

### 3️⃣ Converting PDFs to HTML
To convert PDFs to HTML, use `convert_to_html.py`. This requires `pdf2htmlEX`.

#### Installing `pdf2htmlEX` on Windows
1. Download `pdf2htmlEX` from [Soft RubyPDF](https://soft.rubypdf.com/software/pdf2htmlex-windows-version).
2. Extract the ZIP file.
3. Copy the extracted folder to `D:\pdf2htmlEX` (or any location of your choice).
4. Add the path to the system environment variable:
   - Open **Start Menu** and search for `Environment Variables`.
   - Click **Edit the system environment variables**.
   - Under **System Variables**, find `Path` and click **Edit**.
   - Click **New** and add the path to `pdf2htmlEX.exe` (e.g., `D:\pdf2htmlEX`).
   - Click **OK** to save changes.
5. Restart your terminal (Command Prompt or PowerShell).

#### Example
```sh
python convert_to_html.py
```

Make sure to update the script with the correct path to `pdf2htmlEX.exe` and its data directory. 

In `convert_to_html.py`, update the `pdf2htmlEX_path` and `data_dir` variables to point to where you've installed `pdf2htmlEX`:
```
pdf2htmlEX_path = "D:/pdf2htmlEX-master/pdf2htmlEX.exe"  # Replace with your pdf2htmlEX path
data_dir = "D:/pdf2htmlEX-master/data"  # Replace with your pdf2htmlEX data directory
```
