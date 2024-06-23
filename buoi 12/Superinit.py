from typing import Any


class Document:
    def __init__(self,authors, date) -> None:
        self.authors = authors
        self.date = date

    def getAuthors(self):
        return self.authors

    def addAuthors(self, name):
        self.authors.append(name)

class Book(Document):
    def __init__(self, authors, date, title) -> None:
        super().__init__(authors, date)
        self.title = title 
    
    def getTitle(self):
        return self.title

class Email(Document):
    def __init__(self, authors, date, subject, to) -> None:
        super().__init__(authors, date)
        self.subject = subject
        self.to = to
    
    def getSubject(self):
        return self.subject
    
    def getto(self):
        return self.to

email = Email(["Nguyen Something", "Nguyen"], "01/01/2011", "Something Nguyen", "Nguyen gì đó")
print(email.getAuthors())

book = Book(["Davinci"], "00/00/2000", "Idk")
print(book.getTitle())
