from file_manager import FileManager

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully.")

    def view_books(self):
        if not self.books:
            print("No books available.")
            return

        for book in self.books:
            status = "Available" if book.available else "Borrowed"
            print("\nBook ID:", book.book_id)
            print("Title:", book.title)
            print("Author:", book.author)
            print("Status:", status)

    def register_member(self, member):
        self.members.append(member)
        print("Member registered successfully.")

    def view_members(self):
        if not self.members:
            print("No members registered.")
            return

        for member in self.members:
            print("\nMember ID:", member.member_id)
            print("Name:", member.name)
            print("Borrowed Books:", member.borrowed_books)

    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def borrow_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if member is None:
            print("Member not found.")
            return

        if book is None:
            print("Book not found.")
            return

        if not book.available:
            print("Book is already borrowed.")
            return

        book.available = False
        member.borrow_book(book_id)
        print("Book borrowed successfully.")

    def return_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if member is None:
            print("Member not found.")
            return

        if book is None:
            print("Book not found.")
            return

        if book_id not in member.borrowed_books:
            print("This member did not borrow this book.")
            return

        book.available = True
        member.return_book(book_id)
        print("Book returned successfully.")

    def save_data(self):
        FileManager.save_books(self.books)
        FileManager.save_members(self.members)

    def load_data(self):
        self.books = FileManager.load_books()
        self.members = FileManager.load_members()
