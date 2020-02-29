#! python3
#  simple backup program - just specify folder and extension (if needed)
import os, zipfile

def backup_to_zip(folder, extension=False):

    if extension:
        print("Hi! You are going to backup all {0} files in {1} folder".format(extension, folder))
    else:
        print("Hi! You are going to make full backup of {} folder!".format(folder))

    os.chdir(folder)
    
    number = 1  # will be used in archive name
    while True:
        zip_file_name = os.getcwd() + "_" + str(number) + ".zip"
        if not os.path.exists(zip_file_name):
            break
        number += 1

    zip_backup = zipfile.ZipFile(zip_file_name, 'w')  # creating new zip file
    for folder_name, subfolders, filenames in os.walk(folder):
        print("Current folder name is " + folder_name)  # for logging

        for subfolder in subfolders:
            print("Subfolder of " + folder_name + " is " + subfolder)  # for logging

        for filename in filenames:
            print("File inside " + folder_name + " is " + filename)  # for logging
            if extension:
                ext = os.path.splitext(filename)[1]  # find out file extension
                if ext == extension:
                    zip_backup.write(filename, compress_type=zipfile.ZIP_DEFLATED)
            else:
                zip_backup.write(filename, compress_type=zipfile.ZIP_DEFLATED)

        print('')

backup_to_zip("C:\\devfolder\\1", ".jpg")
