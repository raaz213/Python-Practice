# Q1. Create a Book Class
# Properties: title, author, year
# Method: info() to print book details

class Book:
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year
    def info(self):
        print(f"Title: {self.title}\nAuthor: {self.author}\nYear: {self.year}")
        
b = Book('Muna Madan','Laxmi Prasad Devkota', 2024)
b.info()
        
# Q2. Inherit from Book → EBook Class
# Add: file_size (MB)
# Add method: download() to show download message

class EBook(Book):
    def __init__(self, title, author, year, file_size):
        super().__init__(title, author, year)
        self.file_size = file_size
    def download(self):
        print(f"Downloading {self.title}...")

b = EBook('Muna Madan','Laxmi Prasad Devkota', 2024, 10)
b.info()
b.download()

# Q3. Create Multiple Objects
# Create 2 books and 1 ebook
# Call their methods

# Create 2 Book objects
b1 = Book('Muna Madan','Laxmi Prasad Devkota', 2024)
b2 = Book('Saptakshya','Laxmi Prasad Devkota', 2024)
# Create 1 EBook object
b3 = EBook('Muna Madan','Laxmi Prasad Devkota', 2024, 10)
# Call their methods
b1.info()
b2.info()
b3.info()
b3.download()

# Q4. Use Encapsulation
# Add private _rating to Book

# Create method to safely get/set rating

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__rating = None  # private attribute

    # Setter method
    def set_rating(self, rating):
        if 0 <= rating <= 5:
            self.__rating = rating
        else:
            print("Invalid rating! Please provide a rating between 0 and 5.")

    # Getter method
    def get_rating(self):
        return self.__rating

    def book_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Rating: {self.__rating}")


# Create a book object
book1 = Book("Python for Beginners", "Raj Kumar")

# Set rating
book1.set_rating(4.5)

# Get and display rating
print("Book Rating:", book1.get_rating())

# Show full book info
book1.book_info()
