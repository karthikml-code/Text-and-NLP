import pdfplumber
file = pdfplumber.open('./any_file.pdf')
full_text = []
for page in range(0,len(file.pages)):
    full_text.append(file.pages[page].extract_text())
