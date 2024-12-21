# write a Library class with no_of_books as two instance variables. Write a program to create a library from this library class and show how you can print all books, add a book and get the number of books using different methods. Show that your program doesnot persist the books after r=the program is stopped!
class Library:
    def __init__(self):
        self.noBooks = 0
        self.books = []

    def add_book(self, book_title):
        self.books.append(book_title)
        self.noBooks = len(self.books)
   
    def get_number_of_books(self):
        print(f"The Library has {self.noBooks} books")
        for books in self.books:
            print(books)

my_library = Library()
my_library.add_book("The Great Gatsby")
my_library.add_book("1984")
my_library.add_book("To Kill a Mockingbird")
my_library.get_number_of_books()