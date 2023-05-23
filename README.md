# README Anggota Perpustakaan

Repositori ini berisi implementasi sederhana dari sebuah Anggota Perpustakaan menggunakan Python. Kelas LibraryMember memungkinkan anggota untuk meminjam dan mengembalikan buku dari perpustakaan.

## Penggunaan

1. Buat objek LibraryMember dengan memberikan sebuah nama:

   ```python
   member = LibraryMember("John Doe")
   ```

2. Buat objek Book:

   ```python
   book1 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling")
   book2 = Book("To Kill a Mockingbird", "Harper Lee")
   book3 = Book("1984", "George Orwell")
   ```

3. Meminjam buku:

   ```python
   member.borrow_book(book1)
   member.borrow_book(book2)
   member.borrow_book(book3)
   ```

   Jika buku tersedia, buku akan dipinjam oleh anggota. Jika tidak, pesan akan ditampilkan yang menunjukkan bahwa buku sedang dipinjam oleh orang lain.

4. Menampilkan daftar buku yang dipinjam:

   ```python
   member.display_borrowed_books()
   ```

   Ini akan mencetak judul, penulis, dan status ketersediaan (tersedia atau sedang dipinjam) dari buku yang dipinjam oleh anggota.

5. Mengembalikan buku:

   ```python
   member.return_book(book2)
   ```

   Anggota dapat mengembalikan buku. Jika buku berhasil dikembalikan, pesan akan ditampilkan yang menunjukkan bahwa buku berhasil dikembalikan. Jika buku tidak dipinjam oleh anggota, pesan akan ditampilkan yang menunjukkan bahwa buku tidak dapat dikembalikan.

6. Menampilkan daftar buku yang dipinjam yang terbaru:

   ```python
   member.display_borrowed_books()
   ```

   Ini akan mencetak judul, penulis, dan status ketersediaan (tersedia atau sedang dipinjam) dari buku yang saat ini dipinjam oleh anggota.

## Rincian Kelas

### Book

Kelas Book merepresentasikan sebuah buku dengan atribut-atribut berikut:

- `title`: Judul buku.
- `author`: Penulis buku.
- `is_available`: Sebuah boolean yang menunjukkan ketersediaan buku (`True` jika tersedia, `False` jika sedang dipinjam).

Kelas Book juga memiliki metode-metode berikut:

- `borrow()`: Memungkinkan anggota untuk meminjam buku. Mengembalikan `True` jika buku berhasil dipinjam, dan `False` jika buku sedang dipinjam.
- `return_book()`: Memungkinkan anggota untuk mengembalikan buku.

### LibraryMember

Kelas LibraryMember merepresentasikan seorang anggota perpustakaan dengan atribut-atribut dan metode-metode berikut:

#### Atribut

- `name`: Nama anggota perpustakaan.
- `borrowed_books`: Sebuah list untuk menyimpan buku-buku yang dipinjam oleh anggota.

#### Metode

- `__init__(self, name)`: Menginisialisasi sebuah objek LibraryMember baru dengan nama yang diberikan.
- `borrow_book(self, book)`: Memungkinkan anggota untuk meminjam sebuah
