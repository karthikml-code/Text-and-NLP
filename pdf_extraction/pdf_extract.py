import pdfplumber
file = pdfplumber.open('./any_file.pdf')
full_text = []
for page in range(0,len(file.pages)):
    full_text.append(file.pages[page].extract_text())
    
#here we are extracting the bold text from the pdf since the example contains headings in bold font
headings = []
with file as pdf: 
    for page in range(3,len(file.pages)):
        text = pdf.pages[page]
        bold_text = text.filter(lambda obj: (obj["object_type"] == "char" and "Bold" in obj["fontname"]))
        headings.append(bold_text.extract_text())
        headings.append("\n")
