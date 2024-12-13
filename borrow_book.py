import datetime
import save_all_books
import save_all_borrowers

def borrow_book(all_books, all_borrowers):
    lend_book_search = input("Enter Book Title to Land: ")
    for book in all_books:
        if book["title"] == lend_book_search:
            if book["quantity"] == 0:
                print(f"{book["title"]} is not available to lend.")
                return 
            else:
                b_name = input("Borrower's Name: ")
                b_phone = input("Borrower's Phone Number: ")
                b_book = book["title"]
                b_return_date = (datetime.datetime.now().date() + datetime.timedelta(days=10)).strftime("%d-%m-%Y")

                b_data = {
                    "name":b_name,
                    "phone":b_phone,
                    "b_title":b_book,
                    "return_date":b_return_date
                }
                all_borrowers.append(b_data)
                save_all_borrowers.save_borrower(all_borrowers)

                book["quantity"] = book["quantity"] - 1
                save_all_books.save_all_books(all_books)
                print(f"{book["title"]} book is being lent until {b_return_date}")
                return
    print("Book Not Found!!!")