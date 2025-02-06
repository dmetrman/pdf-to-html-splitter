import os
import subprocess

def convert_pdfs_to_html(input_folder, pdf2htmlEX_path, data_dir):
    """
    Converts PDF files to HTML using pdf2htmlEX.

    Args:
        input_folder (str): Folder containing the PDF files.
        pdf2htmlEX_path (str): Path to the pdf2htmlEX executable.
        data_dir (str): Path to the pdf2htmlEX data directory.
    """
    for filename in os.listdir(input_folder):
        if filename.endswith(".pdf"):
            input_pdf = os.path.join(input_folder, filename)
            output_html = os.path.splitext(filename)[0] + ".html"

            command = [
                pdf2htmlEX_path,
                "--data-dir", data_dir,
                input_pdf,
                output_html
            ]

            try:
                subprocess.run(command, check=True)
                print(f"✅ Converted: {input_pdf} -> {output_html}")
            except subprocess.CalledProcessError as e:
                print(f"❌ Error converting {input_pdf}: {e}")

# Example usage
if __name__ == "__main__":
    input_folder = "output_pdfs"
    pdf2htmlEX_path = "D:/pdf2htmlEX-master/pdf2htmlEX.exe"  # Update with the correct path
    data_dir = "D:/pdf2htmlEX-master/data"  # Update with the correct path

    convert_pdfs_to_html(input_folder, pdf2htmlEX_path, data_dir)
