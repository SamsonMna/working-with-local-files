#finding the file size and folder content
import shutil, os
os.chdir('path/to/directory')
# copying files from one directory to another
shutil.copy('path/to/file', 'path/to/paste/file')
# copying folders at source with its files
shutil.copytree('directory/to/be/copied', 'path/to/paste/directory/to')
# Moving files
shutil.move('path/to/file/for/moving', 'path/to/directory/to/move')
