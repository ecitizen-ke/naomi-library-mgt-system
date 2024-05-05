book=[] #list to store book data

def addBook():
    """
    This function allows adding a new book to the library's collection.
    """
    title=input("Enter book title: ")
    author=input("Enter book author: ")
    book.append({"title":title,"author":author,"checked_out": False})
    print("Book added successfully")

def displayBooks():
    """
    This function displays a list of all books in the library.
    """
    print("Library Books:")
    for index,books in enumerate(book,start=1):
        print(f"{index}. Book: {books['title']}, Author: {books['author']}, Checkout Status: {books['checked_out']}")


def searchBook():
    """
    This function enables searching for a book by title, handling case insensitive searches.
    """
    title=input("Enter book title to search: ")
    for books in book:
        if books['title'].lower() == title.lower(): #ensures no case sensitivity
            print(f"Found: {books['title']} by {books['author']}")
            break
        else:
            print("Book not found")
            break


def checkOut():
    """
    This function allows a user to check out a book from the library.
    """
    title=input("Enter book title to check out: ")
    for books in book:
        if books["title"].lower() == title.lower() and not books["checked_out"]:
            books["checked_out"] = True
            print(f"{books['title']} by {books['author']} checked out successfully")
            return
    print("Book not found or already checked out") 

def returnBook():
    """
    This function enables returning a checked-out book to the library.
    """
    title=input("Enter book title to return: ")
    for books in book:
        if books["title"].lower() == title.lower() and books["checked_out"]:
            books["checked_out"] = False
            print(f"{books['title']} by {books['author']} returned successfully")
            return
    print("Book not found")

def displayCheckedOutBooks():
    """
    This function shows a list of books currently checked out.
    """
    checkedOut=[]
    for books in book:
        if books["checked_out"]:
            checkedOut.append(books)
    for books in checkedOut:
        print(f"{books['title']} by {books['author']} is checked out")
    if not checkedOut:
        print("No books are currently checked out.")
        

def main():
    """
    This function contains the main logic of the program.
    """
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Display All Books")
        print("3. Search For Book by Title")
        print("4. Checkout Book")
        print("5. Return Book")
        print("6. Display Checked Out Books")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            addBook()
        elif choice == "2":
            displayBooks()
        elif choice == "3":
            searchBook()
        elif choice == "4":
            checkOut()
        elif choice == "5":
            returnBook()
        elif choice == "6":
            displayCheckedOutBooks()
        elif choice == "7":
            print("Leaving Library..")
            break
        else:
            print("Invalid. Try Again.")

if __name__ == "__main__":
    main()