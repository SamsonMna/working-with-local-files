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

