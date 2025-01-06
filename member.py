import json
import os
import timer


# Function to load data from JSON files
def load_data(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save data to JSON files
def save_data(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def display_all_members():
    users = load_data('user.json')
    if not users:
        print("No members found.")
        return
    print("List of all members:")
    for user in users:
        print(f"ID: {user['id']}, Name: {user['Name']}, Phone: {user['Phone']}, Address: {user['Address']}")


# 1. Add Member with auto-incrementing ID
def add_member():
    users = load_data('user.json')
    new_id = str(max([int(user['id']) for user in users], default=0) + 1) if users else "1"

    name = input("Enter member name: ")
    tel = input("Enter phone number: ")
    address = input("Enter address: ")
    new_member = {
        "id": new_id,
        "Name": name,
        "Phone": tel,
        "Address": address
    }
    users.append(new_member)
    save_data('user.json', users)
    print(f"Member added successfully with ID {new_id}.")

# 2. Search Member
def search_member():
    users = load_data('user.json')
    search_id = input("Enter member ID to search: ")
    for user in users:
        if user['id'] == search_id:
            print(f"ID: {user['id']}, Name: {user['Name']}, Phone: {user['Phone']}, Address: {user['Address']}")
            return
    print("Member not found.")

# 3. Delete Member
def delete_member():
    users = load_data('user.json')
    delete_id = input("Enter member ID to delete: ")
    for user in users:
        if user['id'] == delete_id:
            users.remove(user)
            save_data('user.json', users)
            print("Member deleted successfully.")
            return
    print("Member not found.")

# 4. Borrow Book
def borrow_book():
    print("Simulating book borrowing...")
    current_time, return_time = timer.loan_dates()

    # Member check
    user_id = input("Enter the member ID: ").strip()
    users = load_data('user.json')

    user = next((user for user in users if user['id'] == user_id), None)
    if not user:
        print("Member not found!")
        return
    print(f"Book borrowed by {user['Name']}")

    # Book check
    books = load_data('kitap.json')
    book_barcode = input("Enter the book barcode: ").strip()
    try:
        book_barcode = int(book_barcode)
    except ValueError:
        print("Invalid barcode! Please enter a numeric barcode.")
        return

    selected_book = next((book for book in books if book['Barkod'] == book_barcode), None)
    if not selected_book:
        print("Book not found!")
        return
    
    track_records = load_data('track.json')
    
    # Check if the book is already in tracking.json (i.e., already borrowed)
    is_book_borrowed = any(record['book_barcode'] == book_barcode for record in track_records)
    
    if is_book_borrowed:
        print(f"The book '{selected_book['Kitap_Adi']}' is already borrowed and cannot be borrowed again.")
        return
    print(f"Book: {selected_book['Kitap_Adi']} by {selected_book['Yazar']}")
    print(f"Borrow Date: {current_time}, Return Date: {return_time}")

    # Save track
    track_data = {
        "user_id": user['id'],
        "user_name": user['Name'],
        "phone": user['Phone'],
        "address": user['Address'],
        "book_barcode": selected_book['Barkod'],
        "book_language": selected_book.get('Dil', 'Bilinmiyor'),
        "book_price": selected_book.get('Fiyat', 'Bilinmiyor'),
        "book_title": selected_book['Kitap_Adi'],
        "book_publisher": selected_book['Yayinevi'],
        "book_author": selected_book['Yazar'],
        "borrow_date": current_time,
        "return_date": return_time
    }
    track_records = load_data('track.json')
    track_records.append(track_data)
    save_data('track.json', track_records)
    print("Book borrowing information saved successfully.")

# 5. Return Book
def return_book():
    print("Simulating book return...")
    user_id = input("Enter the member ID: ")
    track_records = load_data('track.json')

    # Find and display borrowed books by user
    borrowed_books = [record for record in track_records if record['user_id'] == user_id]
    if not borrowed_books:
        print("No books found for this member!")
        return

    print(f"Books borrowed by Member ID {user_id}:")
    for record in borrowed_books:
        print(f"- {record['book_title']} (Return Date: {record['return_date']})")

    # Return logic
    book_barcode = input("Enter the book barcode to return: ")
    track_records = [record for record in track_records if not (record['user_id'] == user_id and str(record['book_barcode']) == book_barcode)]
    save_data('track.json', track_records)
    print("Book returned successfully.")

# 6. Track Book
def track_book():
    print("Simulating book tracking...")
    try:
        # track.json dosyasını UTF-8 ile aç ve oku
        with open('track.json', 'r', encoding='utf-8') as file:
            track_records = json.load(file)
            
            # Eğer kayıtlar varsa, her birini yazdır
            if track_records:
                for record in track_records:
                    print(f"ID: {record['user_id']}")
                    print(f"Name: {record['user_name']}")
                    print(f"Phone: {record['phone']}")
                    print(f"Address: {record['address']}")
                    print(f"Book Title: {record['book_title']}")
                    
                    # Borrow Date ve Return Date'i formatla
                    try:
                        borrow_date, return_date = record['borrow_date'], record['return_date']                    
                    except ValueError:
                        borrow_date = "Invalid Date"
                        return_date = "Invalid Date"
                    
                    print(f"Borrow Date: {borrow_date}")
                    print(f"Return Date: {return_date}")
                    print("-" * 40)  # Her kaydın sonunda ayraç ekle
            else:
                print("No borrowing records found.")
                
    except FileNotFoundError:
        print("No book borrowing records found!")
