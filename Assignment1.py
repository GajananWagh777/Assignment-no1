class Library:
    def __init__(self):
        self.books = []
        self.patrons = []
        self.borrowed = []

    # Add a book
    def add_book(self, book):
        self.books.append(book)
        print(book, 'added successfully.')

    # Register a patron
    def register_patron(self, patron):
        self.patrons.append(patron)
        print(patron, 'registered successfully.')

    # Borrow a book
    def borrow_book(self, name, book):
        if name in self.patrons and book in self.books:
            self.books.remove(book)
            self.borrowed.append([name, book])
            print(name, 'borrowed', book)
        else:
            print("Book or Patron not found.")

    # Return a book
    def return_book(self, name, book):
        if [name, book] in self.borrowed:
            self.borrowed.remove([name, book])
            self.books.append(book)
            print(name, 'returned', book)
        else:
            print("Record not found.")

    # Display available books
    def display_books(self):
        if len(self.books) == 0:
            print("No books available.")
        else:
            print("\nAvailable Books:")
            for book in self.books:
                print(book)

# Object creation and testing
SOC_library = Library()
SOC_library.add_book('Python')
SOC_library.add_book('Java')
SOC_library.add_book('C++')
SOC_library.register_patron('Ajay')
SOC_library.register_patron('Gajanan')
SOC_library.display_books()
SOC_library.borrow_book('Ajay', 'Python')
SOC_library.borrow_book('Gajanan', 'Python')
SOC_library.display_books()
SOC_library.return_book('Ajay', 'Python')
SOC_library.display_books()
      
