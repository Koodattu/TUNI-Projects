from vision_parse import VisionParser

custom_prompt = """
Strictly preserve markdown formatting during text extraction from scanned document.
"""

# Initialize parser with Ollama configuration
parser = VisionParser(
    model_name="llama3.2-vision:11b-instruct-q4_K_M",
    temperature=0.7,
    top_p=0.6,
    num_ctx=4096,
    image_mode="base64",
    custom_prompt=custom_prompt,
    detailed_extraction=True,
    ollama_config={
        "OLLAMA_NUM_PARALLEL": 1,
        "OLLAMA_REQUEST_TIMEOUT": 24000,
        "OLLAMA_HOST": "http://localhost:11434/",
    },
    enable_concurrency=True,
)

# Convert PDF to markdown
pdf_path = "tiekartta.pdf" # local path to your pdf file
markdown_pages = parser.convert_pdf(pdf_path)

# Save markdown to file
markdown_path = "tiekartta.md"
with open(markdown_path, "w") as f:
    f.write("\n\n".join(markdown_pages))