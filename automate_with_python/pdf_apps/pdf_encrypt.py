#! python3
# Simple PDF encryption program

import PyPDF2

pdf_file = open('test2.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

pdf_writer = PyPDF2.PdfFileWriter()

for page_number in range(pdf_reader.numPages):
    pdf_writer.addPage(pdf_reader.getPage(page_number))

pdf_writer.encrypt('qwe123QWE')
result_pdf = open('result-encrypted.pdf', 'wb')
pdf_writer.write(result_pdf)
result_pdf.close()