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
