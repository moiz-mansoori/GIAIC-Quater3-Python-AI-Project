# library_manager.py
# A command-line Personal Library Manager that allows users to manage their book collection.

import os
import json

def clear_screen():
    """Clear the command line screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

class LibraryManager:
    def __init__(self):
        self.library = []
        self.file_path = "library.txt"
        self.load_library()
    
    def add_book(self):
        """Add a new book to the library."""
        print("\n=== Add a Book ===")
        title = input("Enter the book title: ")
        author = input("Enter the author: ")
        
        # Validate publication year input
        while True:
            try:
                year = int(input("Enter the publication year: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid year (integer).")
        
        genre = input("Enter the genre: ")
        
        # Validate read status input
        while True:
            read_status = input("Have you read this book? (yes/no): ").lower()
            if read_status in ["yes", "no"]:
                read_status = read_status == "yes"
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
        
        book = {
            "title": title,
            "author": author,
            "year": year,
            "genre": genre,
            "read": read_status
        }
        
        self.library.append(book)
        print("Book added successfully!")
    
    def remove_book(self):
        """Remove a book from the library."""
        print("\n=== Remove a Book ===")
        if not self.library:
            print("Your library is empty!")
            return
            
        title = input("Enter the title of the book to remove: ")
        found = False
        
        for i, book in enumerate(self.library):
            if book["title"].lower() == title.lower():
                self.library.pop(i)
                print("Book removed successfully!")
                found = True
                break
        
        if not found:
            print("Book not found in your library.")
    
    def search_book(self):
        """Search for a book by title or author."""
        print("\n=== Search for a Book ===")
        if not self.library:
            print("Your library is empty!")
            return
            
        print("Search by:")
        print("1. Title")
        print("2. Author")
        
        while True:
            try:
                choice = int(input("Enter your choice: "))
                if choice in [1, 2]:
                    break
                else:
                    print("Invalid choice. Please enter 1 or 2.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        search_term = input("Enter the title: " if choice == 1 else "Enter the author: ").lower()
        search_key = "title" if choice == 1 else "author"
        
        matching_books = []
        for book in self.library:
            if search_term in book[search_key].lower():
                matching_books.append(book)
        
        if matching_books:
            print("\nMatching Books:")
            self._display_books(matching_books)
        else:
            print("No matching books found.")
    
    def display_all_books(self):
        """Display all books in the library."""
        print("\n=== Your Library ===")
        if not self.library:
            print("Your library is empty!")
            return
            
        self._display_books(self.library)
    
    def _display_books(self, books):
        """Helper method to display a list of books."""
        for i, book in enumerate(books, 1):
            read_status = "Read" if book["read"] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")
    
    def display_statistics(self):
        """Display library statistics."""
        print("\n=== Library Statistics ===")
        if not self.library:
            print("Your library is empty!")
            return
            
        total_books = len(self.library)
        read_books = sum(1 for book in self.library if book["read"])
        percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0
        
        print(f"Total books: {total_books}")
        print(f"Percentage read: {percentage_read:.1f}%")
    
    def save_library(self):
        """Save the library to a file."""
        try:
            with open(self.file_path, 'w') as file:
                json.dump(self.library, file)
            return True
        except Exception as e:
            print(f"Error saving library: {e}")
            return False
    
    def load_library(self):
        """Load the library from a file if it exists."""
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r') as file:
                    self.library = json.load(file)
                return True
            except Exception as e:
                print(f"Error loading library: {e}")
                return False
        return False
    
    def display_menu(self):
        """Display the main menu."""
        clear_screen()
        print("=" * 40)
        print("Welcome to your Personal Library Manager!")
        print("=" * 40)
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        print("=" * 40)
    
    def run(self):
        """Run the library manager program."""
        while True:
            self.display_menu()
            
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("\nInvalid input. Please enter a number.")
                input("Press Enter to continue...")
                continue
            
            if choice == 1:
                self.add_book()
            elif choice == 2:
                self.remove_book()
            elif choice == 3:
                self.search_book()
            elif choice == 4:
                self.display_all_books()
            elif choice == 5:
                self.display_statistics()
            elif choice == 6:
                if self.save_library():
                    print("Library saved to file. Goodbye!")
                else:
                    print("Failed to save library. Goodbye!")
                break
            else:
                print("\nInvalid choice. Please try again.")
            
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    library_manager = LibraryManager()
    library_manager.run()