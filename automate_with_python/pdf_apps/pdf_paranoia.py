#! python3

import os, PyPDF2, sys

print('Hi! This is PDF encryption program. Run the script in required folder')
print('Specify encryption password:')
try:
    password = sys.argv[1]
except:
    print("You haven't specified the password!")

folder = '.'
pdf_list = []
print(os.getcwd())
for folder_name, subfolders, filenames in os.walk(folder):
    for filename in filenames:
        if filename.endswith(".pdf"):
            pdf_list.append(filename)
            real_file_path = os.path.join(folder_name, filename)
            real_folder_path = os.path.join(folder_name)

            pdf_file = open(real_file_path, 'rb')
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)
            pdf_writer = PyPDF2.PdfFileWriter()

            for page_number in range(pdf_reader.numPages):
                pdf_writer.addPage(pdf_reader.getPage(page_number))

            pdf_writer.encrypt(password)
            new_filename = os.path.splitext(filename)[0] + '_encrypted.pdf'
            result_pdf = open(real_folder_path + '/' + new_filename, 'wb')
            pdf_writer.write(result_pdf)
            print('New encrypted version of {0} was created'.format(filename))
            result_pdf.close()

            pdf_encrypted = open(os.path.join(folder_name, new_filename), 'rb')
            pdf_encrypted_reader = PyPDF2.PdfFileReader(pdf_encrypted)
            if pdf_encrypted_reader.decrypt(password) == True:
                print('{0} file can be successfully decrypted'.format(new_filename))
            else:
                print('Cannot decrypt {0} file'.format(new_filename))

            # os.remove(real_folder_path + '/' + 'qqq01.pdf')  # need to fix
# Part 2
# TODO: find all encrypted PDFs in the folder and subfolders
# TODO: create decrypted copy of PDF using the password
# TODO: if password is incorrect - show message and go to the next