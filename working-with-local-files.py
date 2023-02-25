import os
# Checking current working directory
os.getcwd()
os.chdir('path/to/directory')
os.getcwd()
os.makedirs('directory/name')
# Handling Absolute and relative paths
os.path.abspath('.')# abspath being the absolute path  and '.' being the current directory
# checking a scripts' file absolute path
os.path.abspath('.//scripts')

#finding the file size and folder content
import shutil, os
os.chdir('path/to/directory')
# copying files from one directory to another
shutil.copy('path/to/file', 'path/to/paste/file')
# copying folders at source with its files
shutil.copytree('directory/to/be/copied', 'path/to/paste/directory/to')
# Moving files
shutil.move('path/to/file/for/moving', 'path/to/directory/to/move')


# Deleting files
import send2trash
send2trash.sendtotrash('file_to_be_deleted.txt')

# Walking a directory tree
import os
for folderName, subfolders, filenames in os.walk('relative/path/to/a/file')
    print("The current file is " + folderName)# Print the absolute path of the file
    
    for subfolder in subfolders:
        print("SUBFOLDER OF" + folderName ": " + subfolder)# Print the subfolder of the file
    for filename in filenames:
        print("FILE INSIDE " + folderName + ": "+ filename)# Print the filename
        
    print("")

# Compressing files with python
import zipfile, os
os.chdir('path/to/file/for/compression')
fileZip = zipfile.ZipFile('file')
fileZip.namelist() # Lists all files in the compressed file
file.info_size # Shows the amount of storage taken by the file before compression
fileZip.info_size # Shows the compressed file size
fileZip.close() # Exits the compression process


#Extracting from Zip files
import zipfile, os
os.chdir('path/to/file')
fileZip = zipfile.ZipFile('file.zip')
filezip.extractall() # extracts all the files in the files into individual files.
fileZip.close()

# Creating and adding to Zip files
import zipfile
newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('file.py', compress_type=zipfile.ZIP_DEFLATED)# Creates a new file.py and compresses it.
newZip.close()


    

