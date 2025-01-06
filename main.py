import json
import os
import book
import member

def main_menu():
    while True:
        print("--------------------------------------")
        print("       WELCOME TO OUR LIBRARY        ")
        print("--------------------------------------")
        print("-                                    ")
        print("-  1 - MEMBERSHIP OPERATIONS         1")
        print("-  2 - BOOK OPERATIONS               2")
        print("-  0 - EXIT                          0")
        print("-                                    ")
        print("--------------------------------------")
        
        choice = input("Please enter the code for the operation you want to perform: ")
        
        if choice == "1":
            member_menu()
        elif choice == "2":
            book_menu()
        elif choice == "0":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.\n")


def member_menu():
    while True:
        print("--------------------------------------")
        print("-                                    ")
        print("-  MEMBERS                          1")
        print("-  ADD MEMBER                       2")
        print("-  SEARCH MEMBER                    3")
        print("-  DELETE MEMBER                    4")
        print("-  BORROW BOOK                      5")
        print("-  RETURN BOOK                      6")
        print("-  TRACK BOOK                       7")
        print("-  EXIT                             0")
        print("-                                    ")
        print("--------------------------------------")
        
        choice = input("Operation: ")
        
        if choice == "1":
            member.display_all_members()
        elif choice == '2':
            member.add_member()
        elif choice == "3":
            member.search_member()
        elif choice == "4":
            member.delete_member()
        elif choice == "5":
            member.borrow_book()
        elif choice == "6":
            member.return_book()
        elif choice == "7":
            member.track_book()
        elif choice == "0":
            print("Returning to the main menu...\n")
            break
        else:
            print("Invalid choice, please try again.\n")


def book_menu():
    while True:
        print("--------------------------------------")
        print("-                                    ")
        print("-  BOOKS                            1")
        print("-  ADD BOOK                         2")
        print("-  SEARCH BOOK                      3")
        print("-  DELETE BOOK                      4")
        print("-  EXIT                             0")
        print("-                                    ")
        print("--------------------------------------")
        
        choice = input("Operation: ")
        
        if choice == "1":
            book.print_books()
        elif choice == "2":
            book.add_book()
        elif choice == "3":
            book.search_book()
        elif choice == "4":
            book.delete_book()
        elif choice == "0":
            print("Returning to the main menu...\n")
            break
        else:
            print("Invalid choice, please try again.\n")


if __name__ == "__main__":
    main_menu()
