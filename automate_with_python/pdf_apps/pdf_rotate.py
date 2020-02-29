#! python3
#  Simple rotate script

import PyPDF2

degree = 90  # 90, 180, 270, 360
rotate_file = open('test2.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(rotate_file)
page = pdf_reader.getPage(0)
page = page.rotateClockwise(degree)

pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.addPage(page)
result_file = open('rotated1.pdf', 'wb')
pdf_writer.write(result_file)
result_file.close()
rotate_file.close()