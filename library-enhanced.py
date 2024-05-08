import json

class Book:
    """
    This class represents a book with attributes such as title, and author
    """
    def __init__(self,bookId,title,author,checkedOut=False):
        self.bookId=bookId
        self.title=title
        self.author=author
        self.checkedOut=checkedOut

    def __str__(self):
        return f" Book Id: {self.bookId}- Title: {self.title}, Author: {self.author}, Checked Out:{self.checkedOut}"
    
class Library:
    """
    This class manages a collection of books. It has methods to load library data from JSON file,
    save library data to JSON file, add a new book to library,display books in library, 
    search for a book by title, checkout a book, return a book, and display checked-out books
    """
    def __init__(self):
        self.books={}
        self.loadLibrary()

    def loadLibrary(self):
        try:
            with open("library.json", 'r') as file:
                self.books = json.load(file)
        except FileNotFoundError:
            print("Error: The file 'library.json' does not exist.")


    def saveLibrary(self):
        with open("library.json", 'w') as file:
            json.dump(self.books, file) # converts Python objects into appropriate json objects. used when the Python objects have to be stored in a file


    def addBook(self,bookId,title,author):
        """
        This function allows adding a new book to the library's collection.
        """
        if title.lower() and bookId not in self.books:
            self.books[bookId] = {"title": title, "author": author, "checked_out": False}
            self.saveLibrary()
            print("Book saved")
        else:
            print("Book exists")

    def displayBooks(self):
        """
        This function displays a list of all books in the library.
        """
        print("Library Books:")
        for key,value in self.books.items():
            print(f"BookId {key}: {value['title']} by {value['author']}, Checkout status: {value['checked_out']}")

        
    def searchBook(self,title):
        for key,value in self.books.items():
            try:
                if value['title'].title() == title.title():
                    print(f"Found: {value['title']} by {value['author']}, Checkout status: {value['checked_out']}")
                    
            except:
            # elif value['title'].title() != title.title():
                print("Book not found")
            #     break
               
    def checkOut(self,title):
        """
        This function allows a user to check out a book from the library.
        """
        for key,value in self.books.items():
            if value['title'].title() == title.title() and not value['checked_out']:
                value['checked_out']=True
                self.saveLibrary()
                print(f"Book '{value['title']}' checked out successfully!")
                return
        print(f"Book not found or already checked out.")

    def returnBook(self,title):
        """
        This function enables returning a checked-out book to the library.
        """
        for key,value in self.books.items():
            if value['title'].title() == title.title() and value['checked_out']:
                value['checked_out']=False
                self.saveLibrary()
                print(f"Book '{value['title']}' returned successfully!")
                return
        print(f"Book not found.")

    def displayCheckedOutBooks(self):
        """
        This function shows a list of books currently checked out.
        """
        checkedOut=[]
        for book in self.books.values():
            if book['checked_out']:
                checkedOut.append(book)
        for books in checkedOut:
            print(f"{books['title']} by {books['author']} is checked out")
        if not checkedOut:
            print("No books are currently checked out.")

def main():
    """
    This function creates an instance of the library class and loads data from a JSON file 
    called "library.json". It enters a loop where it repeatedly prompts user to choose an action. 
    Depending on the user's choice, it calls the corresponding method of the Library class
    """
    library=Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Display All Books")
        print("3. Search for Book by Title")
        print("4. Checkout Book")
        print("5. Return Book")
        print("6. Display Checked Out Books")
        print("7. Exit")
        choice=input("Enter your choice: ")

        if choice == "1":
            bookId=input("Enter book ID: ")
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.addBook(bookId,title, author)
        elif choice == "2":
            library.displayBooks()
        elif choice == "3":
            title=input("Enter book title: ")
            library.searchBook(title)
        elif choice == "4":
            title=input("Enter book title to checkout: ")
            library.checkOut(title)
        elif choice == "5":
            title=input("Enter book title to return: ")
            library.returnBook(title)
        elif choice == "6":
            library.displayCheckedOutBooks()
        elif choice == "7":
            library.saveLibrary()
            print("Leaving Library..")
            break
        else:
            print("Invalid. Try Again.")

if __name__ == "__main__":
    main()

    