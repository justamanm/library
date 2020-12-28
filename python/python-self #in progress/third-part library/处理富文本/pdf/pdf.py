import pdfplumber

with pdfplumber.open("1.pdf") as pdf:
    print(pdf.pages)
    first_page = pdf.pages[1]
    print(first_page.extract_text())