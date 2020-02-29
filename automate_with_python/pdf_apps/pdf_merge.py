#! python3
# Simple program for several PDF files merge.

import os, PyPDF2

# Get PDF filenames
pdf_list = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdf_list.append(filename)
print(pdf_list)

# Set start page to start merge
start_page = 2  # e.g. first page won't be merged

pdf_writer = PyPDF2.PdfFileWriter()

for file in pdf_list:
    pdf_reader = PyPDF2.PdfFileReader(open(file, 'rb'))
    for page_number in range(start_page - 1, pdf_reader.numPages):
        pdf_writer.addPage(pdf_reader.getPage(page_number))

result_file = open('result.pdf', 'wb')
pdf_writer.write(result_file)
result_file.close()