import json
import os
import tools.timer as timer
import tools.book as book


# Üyeleri JSON dosyasından okuma
def read_users():
    try:
        with open("tools/user.json", "r", encoding="utf-8") as file:
            users = json.load(file)
    except FileNotFoundError:
        users = []  # Dosya yoksa boş bir liste döndür
    return users

# Üyeleri JSON dosyasına yazma
def write_users(users):
    with open("tools/user.json", "w", encoding="utf-8") as file:
        json.dump(users, file, ensure_ascii=False, indent=4)

def display_all_members():
    users = read_users()
    if not users:
        print("No members found.")
        return
    print("List of all members:")
    for user in users:
        print(f"ID: {user['id']}, Name: {user['Name']}, Phone: {user['Phone']}, Address: {user['Address']}")

def add_member():
    users = read_users()
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
    write_users(users)  # Verileri dosyaya yaz
    print(f"Member added successfully with ID {new_id}.")

def search_member():
    users = read_users()
    search_id = input("Enter member ID to search: ")
    for user in users:
        if user['id'] == search_id:
            print(f"ID: {user['id']}, Name: {user['Name']}, Phone: {user['Phone']}, Address: {user['Address']}")
            return
    print("Member not found.")

def delete_member():
    users = read_users()
    delete_id = input("Enter member ID to delete: ")
    for user in users:
        if user['id'] == delete_id:
            users.remove(user)
            write_users(users)  # Güncellenmiş veriyi dosyaya yaz
            print("Member deleted successfully.")
            return
    print("Member not found.")

def read_tracks():
    try:
        with open("tools/track.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def write_tracks(tracks):
    with open("tools/track.json", "w", encoding="utf-8") as file:
        json.dump(tracks, file, ensure_ascii=False, indent=4)

# 4. Borrow Book
def borrow_book():
    print("Simulating book borrowing...")
    current_time, return_time = timer.loan_dates()

    # Member check
    user_id = input("Enter the member ID: ").strip()
    users = read_users()  # load_data yerine read_users

    user = next((user for user in users if user['id'] == user_id), None)
    if not user:
        print("Member not found!")
        return
    print(f"Book borrowed by {user['Name']}")

    # Book check
    books = book.read_books()  # load_data yerine read_books
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
    
    track_records = read_tracks()  # load_data yerine read_tracks
    
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
    track_records.append(track_data)
    write_tracks(track_records)  # save_data yerine write_tracks
    print("Book borrowing information saved successfully.")

# 5. Return Book
def return_book():
    print("Simulating book return...")

    # Kullanıcı ID'si kontrolü
    user_id = input("Enter the member ID: ").strip()
    track_records = read_tracks()  # load_data yerine read_tracks fonksiyonu

    # Kullanıcının borçlu olduğu kitapları bulma
    borrowed_books = [record for record in track_records if record['user_id'] == user_id]
    if not borrowed_books:
        print(f"No books found for Member ID {user_id}.")
        return

    # Borçlu kitapların listesi
    print(f"Books borrowed by Member ID {user_id}:")
    for i, record in enumerate(borrowed_books, start=1):
        print(f"{i}. Book Title: {record['book_title']} (Return Date: {record['return_date']})")

    # Kullanıcıdan iade edilecek kitabın barkodunu isteme
    book_barcode = input("Enter the book barcode to return: ").strip()
    try:
        book_barcode = int(book_barcode)
    except ValueError:
        print("Invalid barcode! Please enter a numeric barcode.")
        return

    # İlgili kitabın kaydını bul ve sil
    book_to_return = next((record for record in borrowed_books if record['book_barcode'] == book_barcode), None)
    if not book_to_return:
        print(f"No borrowed book found with barcode {book_barcode}.")
        return

    # Kayıtları güncelleme
    track_records = [record for record in track_records if record != book_to_return]
    write_tracks(track_records)  # save_data yerine write_tracks fonksiyonu
    print(f"Book '{book_to_return['book_title']}' returned successfully.")

# 6. Track Book
def track_book():
    print("Simulating book tracking...")
    try:
        # track.json dosyasını UTF-8 ile aç ve oku
        with open('tools/track.json', 'r', encoding='utf-8') as file:
            track_records = json.load(file)
            
            # Eğer kayıtlar varsa, her birini yazdır
            if track_records:
                for record in track_records:
                    print(f"ID: {record['user_id']}")
                    print(f"Name: {record['user_name']}")
                    print(f"Phone: {record['phone']}")
                    print(f"Address: {record['address']}")
                    print(f"Book Title: {record['book_title']}")
                    
                    # 'Fiyat' ve 'Dil' anahtarlarını kontrol et
                    book_price = record.get('book_price', 'Bilinmiyor')  # Eger 'Fiyat' yoksa 'Bilinmiyor' yazdır
                    book_language = record.get('book_language', 'Bilinmiyor')  # Eger 'Dil' yoksa 'Bilinmiyor' yazdır
                    
                    print(f"Book Price: {book_price}")
                    print(f"Book Language: {book_language}")
                    print(f"Book Publisher: {record['book_publisher']}")
                    print(f"Book Author: {record['book_author']}")
                    print(f"Borrow Date: {record['borrow_date']}")
                    print(f"Return Date: {record['return_date']}")
                    print("-" * 40)  # Her kaydın sonunda ayraç ekle
            else:
                print("No borrowing records found.")
                
    except FileNotFoundError:
        print("No book borrowing records found!")


