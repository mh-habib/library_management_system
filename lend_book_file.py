import borrow_book
import return_book

def lend_book(all_books, all_borrowers):
    while True:
        print("Welcome to lend book option.")
        print("Enter 0 to go back to the main menu.")
        print("Enter 1 to borrow book.")
        print("Enter 2 to return book.")

        option = input("Please enter a number to choose operation: ")

        if option == "0":
            print("Thanks for using library.")
            return
        elif option == "1":
            borrow_book.borrow_book(all_books, all_borrowers)
        elif option == "2":
            return_book.return_book(all_books, all_borrowers)
        else:
            print("Please enter a valid number!")
        