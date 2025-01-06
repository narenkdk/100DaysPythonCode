#Day 44 - Class definition


#Create a class for a book with attributes like title and author.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"

# Example usage
my_book = Book("One Hundred Years of Solitude", "Gabriel García Márquez")
print(my_book)
