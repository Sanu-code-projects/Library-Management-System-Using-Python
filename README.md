# Library-Management-System-Using-Python

# Library Management System

## Project Overview

The Library Management System is a Python-based command-line application developed to simplify the management of books and library members. The system allows users to add books, register members, borrow books, return books, and save records using CSV files. It demonstrates the application of object-oriented programming concepts and other fundamental Python programming techniques.

---

## Project Purpose

The purpose of this project is to provide a simple and efficient solution for managing library operations while demonstrating the use of Python programming concepts such as classes, objects, methods, loops, conditional statements, file handling, exception handling, and modular programming.

---

## Features

* Add new books
* View all books
* Register new members
* View all members
* Borrow books
* Return books
* Save data using CSV files
* Load saved data automatically when the program starts
* Menu-driven interface
* Exception handling for invalid input

---

## Project Structure

```text
library-management-system/

│── main.py
│── book.py
│── member.py
│── library.py
│── file_manager.py
│── books.csv
│── members.csv
```

---

## Requirements

* Python 3.10 or later
* Visual Studio Code (recommended)

---

## Installation

1. Download or clone this repository.

2. Open the project folder in Visual Studio Code.

3. Ensure Python is installed on your computer.

---

## Running the Program

Open the terminal inside the project folder and run:

```bash
python main.py
```

---

## Example Usage

```text
===== Library Management System =====

1. Add Book
2. View Books
3. Register Member
4. View Members
5. Borrow Book
6. Return Book
7. Save and Exit
```

Example:

```text
Enter your choice: 1

Enter Book ID: B001
Enter Book Title: Python Basics
Enter Author: John Smith

Book added successfully.
```

---

## Files Description

| File            | Description                  |
| --------------- | ---------------------------- |
| main.py         | Main program and menu system |
| book.py         | Book class                   |
| member.py       | Member class                 |
| library.py      | Library operations           |
| file_manager.py | CSV file handling            |
| books.csv       | Stores book records          |
| members.csv     | Stores member records        |

---

## Python Concepts Used

* Object-Oriented Programming (OOP)
* Classes and Objects
* Methods
* Lists
* Loops
* Conditional Statements
* File Handling (CSV)
* Exception Handling
* Modular Programming
* PEP 8 Coding Style

---

## Future Improvements

* Graphical User Interface (GUI)
* SQLite database integration
* Search functionality
* Book categories
* User authentication
* Fine calculation for overdue books

---
