import save_all_borrowers
import save_all_books

def return_book(all_books, all_borrowers):
    book = input("Enter book name: ")
    i_phone = input("Enter phone number: ")
    flag = 0
    for borrower in all_borrowers:
        if borrower["b_title"] == book and borrower["phone"] == i_phone:
            all_borrowers.pop(flag)
            save_all_borrowers.save_borrower(all_borrowers)

            for book in all_books:
                if book["title"] == borrower["b_title"]:
                    book["quantity"] = book["quantity"] + 1
                    save_all_books.save_all_books(all_books)

            print("Thanks for return book timely.")
            return
        flag += 1 

    print("Not match!!!")
    print("Please enter correct information")