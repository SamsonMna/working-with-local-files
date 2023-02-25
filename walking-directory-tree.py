# Walking a directory tree
import os
for folderName, subfolders, filenames in os.walk('relative/path/to/a/file')
    print("The current file is " + folderName)# Print the absolute path of the file
    
    for subfolder in subfolders:
        print("SUBFOLDER OF" + folderName ": " + subfolder)# Print the subfolder of the file
    for filename in filenames:
        print("FILE INSIDE " + folderName + ": "+ filename)# Print the filename
        
    print("")
