# book_class.py

class Book:
    """
    Simple Book class to demonstrate Python magic methods.
    Attributes:
        title (str)
        author (str)
        year (int)
    """

    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = int(year)

    def __str__(self) -> str:
        # Informal / user-friendly string
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self) -> str:
        # Official string that can recreate the object (when Book is in scope)
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        # Destructor: print a message on deletion
        # Note: __del__ may not always run immediately in some environments.
        print(f"Deleting {self.title}")
