# Library Management System

This project is a library management system built using Python. It allows users to manage books and members, track borrowing and returning of books, and maintain records of these activities.

## Features

### Book Management

- **Add Book**: Add new books to the system with details like barcode, title, author, price, language, and publisher.
- **Search Book**: Search for books using title, author, or barcode.
- **Delete Book**: Remove books from the system.
- **View All Books**: Display a list of all books in the library.

### Member Management

- **Add Member**: Add new members to the system with details like name, phone, and address. IDs are auto-incremented.
- **Search Member**: Search for members using their ID.
- **Delete Member**: Remove members from the system.
- **View All Members**: Display a list of all registered members.

### Borrowing and Returning

- **Borrow Book**: Borrow books by members with details of borrowing and return dates.
- **Return Book**: Return borrowed books and update records.
- **Track Borrowed Books**: View the borrowing history of books and members.

## Installation

1. Clone this repository:

   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install required Python packages:

   ```bash
   pip install -r requirements.txt
   ```


Run the application using the following command:

```bash
python main.py
```

### Main Menu

1. Membership Operations
2. Book Operations
3. Exit

#### Membership Operations

1. View all members
2. Add a new member
3. Search for a member
4. Delete a member
5. Borrow a book
6. Return a book
7. Track borrowed books
8. Return to main menu

#### Book Operations

1. View all books
2. Add a new book
3. Search for a book
4. Delete a book
5. Return to main menu

## File Structure

- `main.py`: Entry point for the application. Handles the main menu and navigation between modules.
- `book.py`: Contains functions for book management such as adding, searching, and deleting books.
- `member.py`: Contains functions for member management such as adding, searching, and deleting members, as well as borrowing and returning books.
- `timer.py`: Utility module for calculating borrowing and returning dates.
- `requirements.txt`: Lists all Python dependencies.
- `kitap.json`: Stores book data.
- `user.json`: Stores member data.
- `track.json`: Stores borrowing and returning records.

## Dependencies

The project relies on the following Python packages:

- `cffi==1.17.1`
- `cryptography==43.0.3`
- `cryptography-fernet==0.1.0`
- `fernet==1.0.1`
- `pyaes==1.6.1`
- `pycparser==2.22`
- `PyJWT==2.10.1`
- `tk==0.1.0`

Install them using:

```bash
pip install -r requirements.txt
```

## Data Format

### Books (`kitap.json`)

```json
[
  {
    "Barkod": "123456",
    "Kitap_Adi": "Example Book",
    "Yazar": "Author Name",
    "Fiyat": "20.00",
    "Dil": "English",
    "Yayinevi": "Publisher Name"
  }
]
```

### Members (`user.json`)

```json
[
  {
    "id": "1",
    "Name": "John Doe",
    "Phone": "123456789",
    "Address": "123 Library St"
  }
]
```

### Borrowing Records (`track.json`)

```json
[
  {
    "user_id": "1",
    "user_name": "John Doe",
    "phone": "123456789",
    "address": "123 Library St",
    "book_barcode": "123456",
    "book_language": "English",
    "book_price": "20.00",
    "book_title": "Example Book",
    "book_publisher": "Publisher Name",
    "book_author": "Author Name",
    "borrow_date": "2025-01-01",
    "return_date": "2025-01-15"
  }
]
```
