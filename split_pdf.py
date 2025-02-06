from PyPDF2 import PdfReader, PdfWriter
import os

def split_pdf(input_pdf, output_folder, output_prefix, ranges):
    """
    Splits a PDF into parts based on specified page ranges.

    Args:
        input_pdf (str): Path to the source PDF file.
        output_folder (str): Folder to save the split parts.
        output_prefix (str): Prefix for output filenames.
        ranges (list of tuples): List of page ranges (start, end).
    """
    reader = PdfReader(input_pdf)
    os.makedirs(output_folder, exist_ok=True)

    for i, (start, end) in enumerate(ranges):
        writer = PdfWriter()
        for page_num in range(start - 1, end):
            writer.add_page(reader.pages[page_num])

        output_filename = os.path.join(output_folder, f"{output_prefix}_part{i + 1}.pdf")
        with open(output_filename, "wb") as output_file:
            writer.write(output_file)
        print(f"✅ Saved: {output_filename}")

# Example usage
if __name__ == "__main__":
    input_pdf = "9UKR_A36.pdf"
    output_folder = "output_pdfs"
    output_prefix = "output"
    ranges = [(1, 5), (6, 10), (10, 22)]

    split_pdf(input_pdf, output_folder, output_prefix, ranges)
