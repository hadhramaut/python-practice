#! python3
# Simple PDF overlaying script. The page numbers should be equal

import PyPDF2
simple_pdf = open('test2.pdf', 'rb')
watermark_pdf = open('watermark.pdf', 'rb')

simple_reader = PyPDF2.PdfFileReader(simple_pdf)
watermark_reader = PyPDF2.PdfFileReader(watermark_pdf)

pdf_writer = PyPDF2.PdfFileWriter()

for page_number in range(0, simple_reader.numPages):  # define pages number
    page = simple_reader.getPage(page_number)
    page.mergePage(watermark_reader.getPage(page_number))  # define required page
    pdf_writer.addPage(page)

result_pdf = open('result.pdf', 'wb')
pdf_writer.write(result_pdf)

watermark_pdf.close()
simple_pdf.close()