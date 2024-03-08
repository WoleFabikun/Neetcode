


class Book:
  def __init__(self, title, content, id):
    self.title = title
    self.content = content
    self.lastPage = 0
    self.id = id

  def displayPage(self):
    return  self.content[self.lastPage]
  
  def turnPage(self):
    self.lastPage += 1
    return self.displayPage()
  

class Library:
  def __init__(self):
    self.books = dict()
    self.activeBook = None
    self.idCounter = 0

  def addBook(self, book):
    
