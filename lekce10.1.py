class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def showInfo(self):
        print("Title: {}".format(self.title))
        print("Author: {}".format(self.author))
        print("Pages: {}".format(self.pages))

    def __str__(self):
        return (f"Title: {self.title} author:{self.author} pages:{self.pages}")
book1=Book("python Crash Course", "Eric Matthes", 624)
book2 = Book("JavaScript: The Good parts", "Douglas Crockford", 170)
print(book1)
book1.showInfo()
# print(book1+book2)