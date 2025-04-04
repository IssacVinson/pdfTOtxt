!sudo apt-get update
!sudo apt-get install qpdf
!qpdf /content/sample_data/bible.pdf /content/sample_data/bible_repaired.pdf #replace bible.pdf with your pdf and fix path

!pdfinfo /content/sample_data/bible_repaired.pdf

!sudo apt-get update
!sudo apt-get install tesseract-ocr
!pip install pytesseract PyMuPDF

import fitz
import pytesseract
from PIL import Image

pdf_path = "/content/sample_data/bible_repaired.pdf"
output_path = "/content/sample_data/bible_ocr.txt"

doc = fitz.open(pdf_path)
with open(output_path, "w", encoding="utf-8") as f:
    for page_index, page in enumerate(doc):
        # Render page to a Pixmap
        pix = page.get_pixmap()
        
        # Convert Pixmap to a PIL Image
        mode = "RGBA" if pix.alpha else "RGB"
        img = Image.frombytes(mode, [pix.width, pix.height], pix.samples)
        
        # OCR the image
        text = pytesseract.image_to_string(img)
        
        # Write to the output file
        f.write(f"--- Page {page_index + 1} ---\n")
        f.write(text + "\n")

print(f"OCR complete. Output saved to {output_path}")
