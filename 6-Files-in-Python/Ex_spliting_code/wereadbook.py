def prompt_read_book():
    name = input('Enter the name of the book you just finished reading: ')

    mark_book_as_read(name)


def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = '1'
    save_all_books(books)