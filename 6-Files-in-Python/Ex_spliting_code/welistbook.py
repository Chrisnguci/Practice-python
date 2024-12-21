def list_books():
    for book in get_all_books():
        read = 'YES' if book['read'] == '1' else 'NO'  # book[3] will be a falsy value (0) if not read
        print(f"{book['name']} by {book['author']} — Read: {read}")