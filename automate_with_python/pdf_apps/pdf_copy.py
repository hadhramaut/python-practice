#! python3
#  Copy PDF files using Python

import PyPDF2

pdf_file = open('pdf-test.pdf', 'rb')  # open in read-binary mode

pdf_reader = PyPDF2.PdfFileReader(pdf_file)  # open PDF reader process
pdf_writer = PyPDF2.PdfFileWriter()  # open PDF writer process - blank document

for page_number in range(pdf_reader.numPages):  # get pages number using numPages method
    page_object = pdf_reader.getPage(page_number)  # create page_object and get page for every number
    pdf_writer.addPage(page_object)  # add previous page to new file

pdf_output = open('pdf-test-new.pdf', 'wb')  # set output file parameters, write-binary mode
pdf_writer.write(pdf_output)  # write result to output file
pdf_output.close()  # close output file
pdf_file.close()  # close original file