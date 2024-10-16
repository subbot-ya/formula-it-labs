bytes_for_one_symbol = 4
symbols_one_string = 25
strings_one_page = 50
pages_book = 100
memory_mb = 1.44

memory_bytes = memory_mb * 1024 * 1024
memory_book_bytes = bytes_for_one_symbol * symbols_one_string * strings_one_page * pages_book

number_books = round(memory_bytes / memory_book_bytes)
print("Количество книг, помещающихся на дискету:", number_books)
