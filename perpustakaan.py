class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            return True
        else:
            return False

    def return_book(self):
        self.is_available = True


class LibraryMember:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            print(f"{self.name} berhasil meminjam buku '{book.title}'")
        else:
            print(f"{self.name} tidak dapat meminjam buku '{book.title}', buku sedang dipinjam")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.return_book()
            print(f"{self.name} berhasil mengembalikan buku '{book.title}'")
        else:
            print(f"{self.name} tidak dapat mengembalikan buku '{book.title}', buku tidak dipinjam")

    def display_borrowed_books(self):
        print(f"Daftar Buku yang Dipinjam oleh {self.name}:")
        for book in self.borrowed_books:
            print(f"Judul: {book.title}")
            print(f"Penulis: {book.author}")
            if book.is_available:
                print("Status: Tersedia")
            else:
                print("Status: Dipinjam")
            print("---------------------")


# Membuat objek LibraryMember
member = LibraryMember("John Doe")

# Membuat beberapa objek Book
book1 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("1984", "George Orwell")

# Meminjam buku
member.borrow_book(book1)
member.borrow_book(book2)
member.borrow_book(book3)

# Menampilkan daftar buku yang dipinjam
member.display_borrowed_books()

# Mengembalikan buku
member.return_book(book2)

# Menampilkan daftar buku yang dipinjam setelah pengembalian
member.display_borrowed_books()
