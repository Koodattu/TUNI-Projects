import ollama
import fitz  # PyMuPDF
import ollama  # Ollama Python library
from PIL import Image
import pytesseract
import ollama
import os

# --- Configuration ---
pdf_path = "tiekartta.pdf"  # Path to your PDF file
output_folder = "outputs"
os.makedirs(output_folder, exist_ok=True)

# Filenames for the three methods' outputs:
ollama_md_file = os.path.join(output_folder, "output_ollama.md")
ocr_md_file = os.path.join(output_folder, "output_ocr.md")
pdf_text_md_file = os.path.join(output_folder, "output_pdf_text.md")

# Temporary folder to store images (used by Ollama and OCR approaches)
temp_image_folder = "temp_images"
os.makedirs(temp_image_folder, exist_ok=True)

# --- Implementation 1: Ollama Vision Approach ---
def process_with_ollama_vision(pdf_path, output_md):
    print("==> Processing PDF with Ollama Vision approach...")
    doc = fitz.open(pdf_path)
    markdown_pages = []
    
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        # Render page at default scale (can adjust if needed)
        pix = page.get_pixmap()
        image_filename = os.path.join(temp_image_folder, f"ollama_page_{page_num+1}.png")
        pix.save(image_filename)
        print(f"Ollama: Saved page {page_num+1} as {image_filename}")
        
        # Call the Ollama vision model with the image file.
        try:
            response = ollama.chat(
                model="llama3.2-vision:11b-instruct-q4_K_M",
                messages=[{
                    "role": "user",
                    "content": "Convert this image into markdown format.",
                    "images": [image_filename]
                }]
            )
            md_text = response.get("message", {}).get("content", "")
            markdown_pages.append(f"## Page {page_num+1}\n\n" + md_text)
            print(f"Ollama: Processed page {page_num+1}.")
        except Exception as e:
            error_msg = f"<!-- Error processing page {page_num+1}: {e} -->"
            markdown_pages.append(error_msg)
            print(f"Ollama: Error on page {page_num+1}: {e}")
    
    with open(output_md, "w", encoding="utf-8") as f:
        f.write("\n\n".join(markdown_pages))
    print(f"Ollama Vision markdown saved to {output_md}")


# --- Implementation 2: OCR Approach with Tesseract ---
def process_with_ocr(pdf_path, output_md, scale_factor=3.0):
    print("==> Processing PDF with Tesseract OCR approach...")
    doc = fitz.open(pdf_path)
    markdown_pages = []
    
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        # Increase resolution by using a transformation matrix with scale_factor.
        mat = fitz.Matrix(scale_factor, scale_factor)
        pix = page.get_pixmap(matrix=mat)
        image_filename = os.path.join(temp_image_folder, f"ocr_page_{page_num+1}.png")
        pix.save(image_filename)
        print(f"OCR: Saved high-res image for page {page_num+1} as {image_filename}")
        
        # Open image with PIL and use pytesseract to perform OCR.
        try:
            img = Image.open(image_filename)
            text = pytesseract.image_to_string(img)
            # Wrap the extracted text in markdown format.
            page_md = f"## Page {page_num+1}\n\n" + text
            markdown_pages.append(page_md)
            print(f"OCR: Processed page {page_num+1}.")
        except Exception as e:
            error_msg = f"<!-- OCR error on page {page_num+1}: {e} -->"
            markdown_pages.append(error_msg)
            print(f"OCR: Error on page {page_num+1}: {e}")
    
    with open(output_md, "w", encoding="utf-8") as f:
        f.write("\n\n".join(markdown_pages))
    print(f"OCR markdown saved to {output_md}")


# --- Implementation 3: Direct PDF Text Extraction Approach ---
def process_with_pdf_text(pdf_path, output_md):
    print("==> Processing PDF with direct text extraction approach...")
    doc = fitz.open(pdf_path)
    markdown_pages = []
    
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        try:
            text = page.get_text()  # Extracts text from the page
            page_md = f"## Page {page_num+1}\n\n" + text
            markdown_pages.append(page_md)
            print(f"PDF Text: Processed page {page_num+1}.")
        except Exception as e:
            error_msg = f"<!-- Text extraction error on page {page_num+1}: {e} -->"
            markdown_pages.append(error_msg)
            print(f"PDF Text: Error on page {page_num+1}: {e}")
    
    with open(output_md, "w", encoding="utf-8") as f:
        f.write("\n\n".join(markdown_pages))
    print(f"Direct PDF text markdown saved to {output_md}")


# --- Main: Run all three approaches ---
if __name__ == "__main__":
    #process_with_ollama_vision(pdf_path, ollama_md_file)
    process_with_ocr(pdf_path, ocr_md_file, scale_factor=3.0)
    process_with_pdf_text(pdf_path, pdf_text_md_file)
    
    print("All processing completed. Compare the markdown files in the 'outputs' folder.")