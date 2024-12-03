class Book:
    def __init__(self, title, author, year):
        """
        Book კლასის ინიციალიზაცია.
        :param title: წიგნის სათაური (str)
        :param author: წიგნის ავტორი (str)
        :param year: გამოცემის წელი (int)
        """
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        """
        წიგნის ინფორმაციის სთრინგის ფორმატში დაბრუნება.
        :return: წიგნის დეტალები (str)
        """
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


class BookManager:
    def __init__(self):
        """
        ინიციალიზაცია: წიგნების ცარიელი სიის შექმნა.
        """
        self.books = []

    def add_book(self, title, author, year):
        """
        წიგნის დამატება სიისთვის.
        :param title: წიგნის სათაური (str)
        :param author: წიგნის ავტორი (str)
        :param year: გამოცემის წელი (int)
        """
        book = Book(title, author, year)
        self.books.append(book)
        print(f"Book '{title}' added successfully!")

    def list_books(self):
        """
        ყველა წიგნის სიის ჩვენება.
        """
        if not self.books:
            print("No books available.")
        else:
            print("Books in the collection:")
            for idx, book in enumerate(self.books, start=1):
                print(f"{idx}. {book}")

    def find_book(self, title):
        """
        წიგნის ძიება სათაურის მიხედვით.
        :param title: საძიებო სათაური (str)
        :return: ნაპოვნი წიგნი ან None
        """
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None


def main_menu():
    """
    აპლიკაციის მთავარი მენიუ.
    """
    print("\nBook Management Application")
    print("1. Add a new book")
    print("2. List all books")
    print("3. Search for a book by title")
    print("4. Exit")


def main():
    """
    მთავარი ფუნქცია, რომელიც მართავს პროგრამის ნაკადს.
    """
    manager = BookManager()  # BookManager კლასის ობიექტი

    while True:
        main_menu()
        choice = input("\nChoose an option (1-4): ")

        if choice == "1":
            # ახალი წიგნის დამატება
            title = input("Enter book title: ").strip()
            author = input("Enter book author: ").strip()
            try:
                year = int(input("Enter book year of publication: ").strip())
            except ValueError:
                print("Invalid year. Please enter a valid number.")
                continue
            manager.add_book(title, author, year)

        elif choice == "2":
            # ყველა წიგნის სიის ჩვენება
            manager.list_books()

        elif choice == "3":
            # ძიება სათაურის მიხედვით
            title = input("Enter the title to search: ").strip()
            book = manager.find_book(title)
            if book:
                print(f"\nFound: {book}")
            else:
                print("\nBook not found.")

        elif choice == "4":
            # პროგრამის დასრულება
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
