from book import Book
from library import Library
from member import Member

library = Library()
library.load_data()

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Register Member")
    print("4. View Members")
    print("5. Borrow Book")
    print("6. Return Book")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_id = input("Enter book ID: ")
        title = input("Enter book title: ")
        author = input("Enter author name: ")

        new_book = Book(book_id, title, author)

        library.add_book(new_book)
    
    elif choice == "2":
        library.view_books()

    elif choice == "3":
         member_id = input("Enter member ID: ")
         name = input("Enter member name: ")

         new_member = Member(member_id, name)

         library.register_member(new_member)

    elif choice == "4":
         library.view_members()   

    elif choice == "5":
         member_id = input("Enter member ID: ")
         book_id = input("Enter book ID: ")

         library.borrow_book(member_id, book_id)

    elif choice == "6":
         member_id = input("Enter member ID: ")
         book_id = input("Enter book ID: ")

         library.return_book(member_id, book_id)

    elif choice == "7":
        library.save_data()
        print("Data saved successfully.")
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")