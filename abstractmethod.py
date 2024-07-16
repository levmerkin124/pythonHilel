from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, title, author_or_director, year):
        self.title = title
        self.author_or_director = author_or_director
        self.year = year

    @abstractmethod
    def description(self):
        return f"Title: {self.title}, Author/Director: {self.author_or_director}, Year: {self.year}"

class Book(LibraryItem):
    def __init__(self, title, author, year, number_of_pages):
        super().__init__(title, author, year)
        self.number_of_pages = number_of_pages

    def description(self):
        return f"{super().description()}, Pages: {self.number_of_pages}"

class Magazine(LibraryItem):
    def __init__(self, title, author, year, issue_number):
        super().__init__(title, author, year)
        self.issue_number = issue_number

    def description(self):
        return f"{super().description()}, Issue Number: {self.issue_number}"

class DVD(LibraryItem):
    def __init__(self, title, director, year, duration):
        super().__init__(title, director, year)
        self.duration = duration

    def description(self):
        return f"{super().description()}, Duration: {self.duration} minutes"

book = Book("Kill him", "Tom Krus", 1945, 3)
magazine = Magazine("Forest Gump", "Tom Hanks", 2023, 7)
dvd = DVD("My love", "Christopher Nolan", 2005, 148)

