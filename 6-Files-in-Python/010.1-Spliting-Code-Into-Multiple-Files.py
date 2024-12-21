
print(globals())
name = 'n'


#1.Separating concerns and ease of organization
'''
For example,
we might have one file for user interaction 
(prints and inputs), and another file for data storage (saving and retrieving things from a file).
'''
#2. Improved readability
'''Navigating theses smaller files will be easier 
and so will understanding the content of each of these files.'''

#3. Easier to reuse code
'''When you have multiple smaller, focused files,
 it's easier to reuse the contents of one file in multiple other files by importing.'''

## How to split a Python file into multiple files

import myfile 
print("What's going on")
'''
output:
	Hello, world!
	What's going on?
->The myfile.py was executed


Note: It's rare that you'll write code like this. 
	Instead, the files you import will normally contain variables and functions, 
	so that when you import them nothing actually happens until you actually use those variables and functions.
'''

#note : Your files work in the same way as modules
# Everything we could do with external modules, we can do with our own files:

#Using files and folders
'''When importing, the dot (.) means something like "inside".

If you have multiple sub-folders, you will need to use multiple . 
to separate the different levels of folders and files, like this:

from folder.subfolder.module import something_in_the_module

'''

#Script mode vs. module mode

'''
When we Run a file, we say that file is ran in "script mode".
When we Import a file, that file runs in "module mode".

1.The file that we run always has a __name__ variable with a value of "__main__". 
That is simply how Python tells us that we ran that file.
2. Any file that doesn't have a __name__ equal to "__main__" Was Imported.
ref: https://teclado.com/30-days-of-python/python-30-day-21-multiple-files/
'''

#Running code only in script mode
'''
__name__ must be equal to "__main__" for a file to have been run.

'''
def get_user_age():
    return int(input("Enter your age: "))

if __name__ == "__main__":
    get_user_age()

'''Giờ mình có thể lý giải tại sao mà đặt if __name__ = "__main__" ở cuối mỗi file quan trọng
là để: Khi chủ đích là chạy file đấy thì file đó mới chạy 1 chức năng nào đó. Còn, nếu là import vào 1 module, file khác thì
hàm đó k được gọi để chạy 1 chức năng nào đó-> import mode
'''
# in the myfile.py module
def get_user_age():
    return int(input("Enter your age: "))

def main():
    print("run the main file")
if __name__ == "__main__": # when run the myfile.py
    main()
# in the main.py:
import user_interactions.myfile # Module mode -> Do not call the main file

user_interactions.myfile.get_user_age()




