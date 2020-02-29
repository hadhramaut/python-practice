class pdf_work():
    def __init__(self):
        pass

    def pdf_merge(self, path, result_file_name, start_page):

        # Simple function for several PDF files merge.

        import os, PyPDF2

        # Get PDF filenames
        pdf_list = []
        for filename in os.listdir(path):
            if filename.endswith('.pdf'):
                pdf_list.append(filename)
        print(pdf_list)

        pdf_writer = PyPDF2.PdfFileWriter()

        for file in pdf_list:
            pdf_reader = PyPDF2.PdfFileReader(open(file, 'rb'))
            for page_number in range(start_page - 1, pdf_reader.numPages):
                pdf_writer.addPage(pdf_reader.getPage(page_number))

        result_file = open(result_file_name, 'wb')
        pdf_writer.write(result_file)
        result_file.close()

    def pdf_encrypt(self, original_pdf, encrypted_pdf, password):

        # Simple PDF encryption function.

        import PyPDF2

        pdf_file = open(original_pdf, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)

        pdf_writer = PyPDF2.PdfFileWriter()

        for page_number in range(pdf_reader.numPages):
            pdf_writer.addPage(pdf_reader.getPage(page_number))

        pdf_writer.encrypt(password)
        result_pdf = open(encrypted_pdf, 'wb')
        pdf_writer.write(result_pdf)
        result_pdf.close()

    def pdf_watermark(self, original_file, watermark_file, result_file):

        # Simple PDF overlaying function. The page numbers should be equal

        import PyPDF2

        simple_pdf = open(original_file, 'rb')
        watermark_pdf = open(watermark_file, 'rb')

        simple_reader = PyPDF2.PdfFileReader(simple_pdf)
        watermark_reader = PyPDF2.PdfFileReader(watermark_pdf)

        pdf_writer = PyPDF2.PdfFileWriter()

        for page_number in range(0, simple_reader.numPages):  # define pages number
            page = simple_reader.getPage(page_number)
            page.mergePage(watermark_reader.getPage(page_number))  # define required page
            pdf_writer.addPage(page)

        result_pdf = open(result_file, 'wb')
        pdf_writer.write(result_pdf)

        watermark_pdf.close()
        simple_pdf.close()

    def pdf_rotate(self, original_pdf, result_pdf, degree_value):

        #  Simple PDF rotate function

        import PyPDF2

        rotate_file = open(original_pdf, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(rotate_file)
        page = pdf_reader.getPage(0)
        page = page.rotateClockwise(degree_value)

        pdf_writer = PyPDF2.PdfFileWriter()
        pdf_writer.addPage(page)
        result_file = open(result_pdf, 'wb')
        pdf_writer.write(result_file)
        result_file.close()
        rotate_file.close()

    def pdf_copy(self, original_file, result_file):

        # Simple PDF copy function

        import PyPDF2

        pdf_file = open(original_file, 'rb')  # open in read-binary mode

        pdf_reader = PyPDF2.PdfFileReader(pdf_file)  # open PDF reader process
        pdf_writer = PyPDF2.PdfFileWriter()  # open PDF writer process - blank document

        for page_number in range(pdf_reader.numPages):  # get pages number using numPages method
            page_object = pdf_reader.getPage(page_number)  # create page_object and get page for every number
            pdf_writer.addPage(page_object)  # add previous page to new file

        pdf_output = open(result_file, 'wb')  # set output file parameters, write-binary mode
        pdf_writer.write(pdf_output)  # write result to output file
        pdf_output.close()  # close output file
        pdf_file.close()  # close original file