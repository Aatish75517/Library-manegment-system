import random
import string
def captcha_check(func):
    def wrapper():
        captcha_text = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
        print("🔐 CAPTCHA:", captcha_text)
        user_input = input("Enter the CAPTCHA shown above: ")

        if user_input == captcha_text:
            print("✅ CAPTCHA Verified! Proceeding...\n")
            func()
        else:
            print("❌ Incorrect CAPTCHA. Try again.") 
    return wrapper
@captcha_check
def library_management_system():
    a = [["english", "john"], ["python", "harry"]]
    issue = []
    while True:
        def add():
            b = input("Enter the name of the book: ")
            c = input("Enter the author of the book: ")
            if any(b.lower() == book[0].lower() and c.lower() == book[1].lower() for book in a):
                print("This book is already in the library.")
            else:
                a.append([b, c])
                print("Added successfully")
        def delete():
            b = input("Enter your book name: ").lower()
            found = False
            for i in a:
                if b == i[0].lower():
                    print("Book:", i[0])
                    print("Author:", i[1])
                    d = input("Do you want to delete? ").lower()
                    if d == "yes":
                        a.remove(i)
                        print("Deleted successfully")
                    else:
                        print("Not deleted")
                    found = True
                    break
            if not found:
                print("Book not found")
        def update():
            b = input("Enter your book name: ").lower()
            found = False
            for i in a:
                if b == i[0].lower():
                    print("Book:", i[0])
                    print("Author:", i[1])
                    d = input("Enter new book name: ")
                    e = input("Enter new author name: ")
                    i[0] = d
                    i[1] = e
                    print("Updated successfully")
                    found = True
                    break
            if not found:
                print("Book not found")
        def search():
            b = input("Enter book name: ").lower()
            found = False
            for i in a:
                if b in i[0].lower():
                    print("Book:", i[0])
                    print("Author:", i[1])
                    found = True
                    break
            if not found:
                print("Book not found")
        def viewall():
            print("All books in the library:")
            for i, j in enumerate(a, start=1):
                print(f"{i}. Book: {j[0]}, Author: {j[1]}")
            input("Press any key to continue")
        def issuebook():
            b = input("Enter book name to issue: ").lower()
            found = False
            for i in a:
                if b == i[0].lower():
                    print("Book:", i[0])
                    print("Author:", i[1])
                    d = input("Do you want to issue? ").lower()
                    if d == "yes":
                        e = input("Enter your name: ")
                        issue.append([i[0], i[1], e])
                        print("Issued successfully")
                    else:
                        print("Not issued")
                    found = True
                    break
            if not found:
                print("Book not found")
        def returnbook():
            b = input("Enter book name to return: ").lower()
            found = False
            for idx, i in enumerate(issue):
                if b == i[0].lower():
                    print("Book:", i[0])
                    print("Author:", i[1])
                    d = input("Do you want to return? ").lower()
                    if d == "yes":
                        a.append([i[0], i[1]])
                        issue.pop(idx)
                        print("Returned successfully")
                    else:
                        print("Not returned")
                    found = True
                    break
            if not found:
                print("Book not found")
        def viewissued():
            if not issue:
                print("No books have been issued.")
            else:
                print("Issued books:")
                for i, j in enumerate(issue, start=1):
                    print(f"{i}. Book: {j[0]}, Author: {j[1]}, Issued to: {j[2]}")
            input("Press any key to continue")
        print("\nLibrary Management System")
        print("1. Admin")
        print("2. User")
        print("3. Exit")
        c = input("Enter your choice: ")
        if c == "1":
            password = input("Enter password: ")
            if password != "123":
                print("Wrong password")
            else:
                print("1. Add book")
                print("2. Delete book")
                print("3. Update book")
                print("4. Search book")
                print("5. View all books")
                print("6. Issue book")
                print("7. Return book")
                print("8. View issued books")
                print("9. Exit")
                d = input("Enter your choice: ")
                if d == "1":
                    add()
                elif d == "2":
                    delete()
                elif d == "3":
                    update()
                elif d == "4":
                    search()
                elif d == "5":
                    viewall()
                elif d == "6":
                    issuebook()
                elif d == "7":
                    returnbook()
                elif d == "8":
                    viewissued()
                elif d == "9":
                    print("Exiting Admin panel.")
                    break
        elif c == "2":
            print("1. Search book")
            print("2. View all books")
            print("3. Issue book")
            print("4. Return book")
            d = input("Enter your choice: ")
            if d == "1":
                search()
            elif d == "2":
                viewall()
            elif d == "3":
                issuebook()
            elif d == "4":
                returnbook()
        elif c == "3":
            print("Exiting Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
library_management_system()
