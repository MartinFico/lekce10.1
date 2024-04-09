class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def showInfo(self):
        print("Title: {}".format(self.title))
        print("Author: {}".format(self.author))
        print("Pages: {}".format(self.pages))
book1=Book("python Crash Course", "Eric Matthes", 624)
book2 = Book("JavaScript: The Good parts", "Douglas Crockford", 170)
print(book1+book2)