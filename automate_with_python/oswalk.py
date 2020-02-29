#! python3
#  demonstration of os.walk method
import os

check_folder = "" #  define the folder
for folderName, subfolders, filenames in os.walk(check_folder): 
    print("Current folder name is " + folderName)

    for subfolder in subfolders:
        print("Subfolder of " + folderName + " is " + subfolder)

    for filename in filenames:
        print("File inside " + folderName + " is " + filename)

    print("")
