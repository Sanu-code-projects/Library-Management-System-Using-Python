import csv

from book import Book
from member import Member


class FileManager:

    @staticmethod
    def save_books(books):
        with open("books.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            writer.writerow(
                ["book_id", "title", "author", "available"]
            )

            for book in books:
                writer.writerow([
                    book.book_id,
                    book.title,
                    book.author,
                    book.available
                ])

    @staticmethod
    def load_books():
        books = []

        try:
            with open("books.csv", "r", encoding="utf-8") as file:
                reader = csv.reader(file)

                next(reader, None)

                for row in reader:
                    book = Book(
                        row[0],
                        row[1],
                        row[2]
                    )

                    book.available = row[3] == "True"

                    books.append(book)

        except FileNotFoundError:
            pass

        return books

    @staticmethod
    def save_members(members):
        with open("members.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            writer.writerow(
                ["member_id", "name", "borrowed_books"]
            )

            for member in members:
                writer.writerow([
                    member.member_id,
                    member.name,
                    ",".join(member.borrowed_books)
                ])

    @staticmethod
    def load_members():
        members = []

        try:
            with open("members.csv", "r", encoding="utf-8") as file:
                reader = csv.reader(file)

                next(reader, None)

                for row in reader:
                    member = Member(
                        row[0],
                        row[1]
                    )

                    if row[2]:
                        member.borrowed_books = row[2].split(",")

                    members.append(member)

        except FileNotFoundError:
            pass

        return members