# Day 21 Exercise - 30 Days Of Python
# Your task is to split this code into files.
# Create a new repl and split the code how you see fit!



from Ex_spliting_code.welistbook import list_books
from Ex_spliting_code.interactingbook import *


USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit
Your choice: """



def menu():
    create_book_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()

        user_input = input(USER_CHOICE)










if __name__ == '__main__':
            menu()