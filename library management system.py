# Library Management System with Input Validation

class Library:
    def __init__(self):
        # Initial book records pre-loaded into the system
        self.books = [
            {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "isbn": "9780743273565", "available": True},
            {"title": "To Kill a Mockingbird", "author": "Harper Lee", "isbn": "9780061120084", "available": True},
            {"title": "1984", "author": "George Orwell", "isbn": "9780451524935", "available": True},
            {"title": "Pride and Prejudice", "author": "Jane Austen", "isbn": "9781503290563", "available": True},
            {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "isbn": "9780316769488", "available": True}
        ]

    def add_book(self):
        """Adds a new book to the library."""
        title = input("Enter the book title: ").strip()
        while not title:
            print("Title cannot be empty.")
            title = input("Enter the book title: ").strip()

        author = input("Enter the author name: ").strip()
        while not author:
            print("Author name cannot be empty.")
            author = input("Enter the author name: ").strip()

        isbn = input("Enter the ISBN number (13 digits): ").strip()
        while not isbn.isdigit() or len(isbn) != 13:
            print("Invalid ISBN. Please enter a 13-digit number.")
            isbn = input("Enter the ISBN number (13 digits): ").strip()

        book = {
            "title": title,
            "author": author,
            "isbn": isbn,
            "available": True
        }
        
        self.books.append(book)
        print(f"Book '{title}' by {author} added successfully!")

    def search_book(self):
        """Search for a book by title or author."""
        search_term = input("Enter the title or author to search: ").strip().lower()
        if not search_term:
            print("Search term cannot be empty.")
            return

        found_books = [book for book in self.books if search_term in book["title"].lower() or search_term in book["author"].lower()]
        
        if found_books:
            print("Search Results:")
            for book in found_books:
                status = "Available" if book["available"] else "Checked Out"
                print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}, Status: {status}")
        else:
            print("No books found with that title or author.")

    def checkout_book(self):
        """Check out a book by ISBN."""
        isbn = input("Enter the ISBN of the book to check out: ").strip()
        if not isbn.isdigit() or len(isbn) != 13:
            print("Invalid ISBN. Please enter a valid 13-digit number.")
            return

        for book in self.books:
            if book["isbn"] == isbn:
                if book["available"]:
                    book["available"] = False
                    print(f"Book '{book['title']}' checked out successfully!")
                else:
                    print(f"Book '{book['title']}' is already checked out.")
                return
        print("Book not found.")

    def checkin_book(self):
        """Check in a book by ISBN."""
        isbn = input("Enter the ISBN of the book to check in: ").strip()
        if not isbn.isdigit() or len(isbn) != 13:
            print("Invalid ISBN. Please enter a valid 13-digit number.")
            return

        for book in self.books:
            if book["isbn"] == isbn:
                if not book["available"]:
                    book["available"] = True
                    print(f"Book '{book['title']}' checked in successfully!")
                else:
                    print(f"Book '{book['title']}' is already checked in.")
                return
        print("Book not found.")

    def display_books(self):
        """Display all books in the library."""
        if not self.books:
            print("The library has no books.")
            return
        
        print("Library Inventory:")
        for book in self.books:
            status = "Available" if book["available"] else "Checked Out"
            print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}, Status: {status}")

def main():
    library = Library()
    
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Search Book")
        print("3. Check Out Book")
        print("4. Check In Book")
        print("5. Display All Books")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()
        while not choice.isdigit() or int(choice) not in range(1, 7):
            print("Invalid choice. Please enter a number from 1 to 6.")
            choice = input("Enter your choice (1-6): ").strip()

        choice = int(choice)
        
        if choice == 1:
            library.add_book()
        elif choice == 2:
            library.search_book()
        elif choice == 3:
            library.checkout_book()
        elif choice == 4:
            library.checkin_book()
        elif choice == 5:
            library.display_books()
        elif choice == 6:
            print("Exiting the system. Goodbye!")
            break

# Run the main program
if __name__ == "__main__":
    main()
