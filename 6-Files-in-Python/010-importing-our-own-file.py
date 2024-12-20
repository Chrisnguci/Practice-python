''' Allowing the file we are currently working on to use code defined in some other file
'''
'''# 2 ways

#1. Import something : it is  a module
import file_operations # A module

file_operations.save_to_file('Chris','name.txt')

#2.from -> import

from file_operations import read_file # become globally in this script

print(read_file('name.txt'))'''

# Part2 : Move to other dir
# Solve: 1. Import the fulpath from top level folder
#
from utils.file_operations import read_file # Utils is a Python package
print(read_file('name.txt'))


# To tell python utils is python package before you can import anything from it
# 