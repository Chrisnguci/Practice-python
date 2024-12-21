import json

BOOKS_FILE = 'books.json'

def create_book_table():
    try:
        with open(BOOKS_FILE, 'x') as file:
            json.dump([], file)  # initialize file as empty list
    except FileExistsError:
        pass


def prompt_add_book():
    name = input('Enter the new book name: ')
    author = input('Enter the new book author: ')

    insert_book(name, author)


def insert_book(name, author):
    books = get_all_books()
    books.append({'name': name, 'author': author, 'read': False})
    save_all_books(books)


def get_all_books():
    with open(BOOKS_FILE, 'r') as json_file:
        return json.load(json_file)


def save_all_books(books):
    with open(BOOKS_FILE, 'w') as file:
        json.dump(books, file)

def prompt_delete_book():
    name = input('Enter the name of the book you wish to delete: ')

    delete_book(name)


def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    save_all_books(books)
