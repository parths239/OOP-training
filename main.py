# Creating book library

class book:
  
  def __init__(self, title, author, isbn):
    self.title = title
    self.author = author
    self.isbn = isbn
    self.is_checked_out = False
  
  # checks out the book
  def check_out(self):
      self.is_checked_out = True
  
  def check_in(self):
    self.is_checked_out = False
    
  def __str__(self) -> str:
    status = "Checked out" if self.is_checked_out else "Available"
    return f"\n Book details: \n Title: {self.title} \n Author: {self.author} \n ISBN: {self.isbn} \n Availability: {status}"
  

class patron(book):
  
  def __init__(self, name, patron_id) :
    self.name = name
    self.patron_id = patron_id
    self.checked_out_books = []
  
  def check_out_book(self,book):
    if not book.is_checked_out:
      self.checked_out_books.append(book)
      book.check_out()
    else:
     return f"The Book {book} is already checked out"
    #return None
  
  def return_book(self,book):
    
    if book in self.checked_out_books:
      self.checked_out_books.remove(book)
      book.check_in()
    else:
      return f"The book {book} was not checked out by {self.name}"
  

    
  def __str__(self):
    
    book_title = [book.title for book in self.checked_out_books]
    
    return f"Patron details: \n Name: {self.name} \n Patron ID: {self.patron_id} \n Checked out books: {' ,'.join(book_title) if book_title else 'None'}"
  

class Library():
  
  def __init__(self) -> None:
    self.books = []
    self.patrons = []
    
  
  def add_book(self,book):
    self.books.append(book)
    
  def add_patron(self, patron):
    self.patrons.append(patron)
    
  def find_book_by_title(self, title):
    for book in self.books:
      if book.title.lower() == title.lower():
        return book
      else:
        return print(f"The book {title} is not in the library")
    
    
  def find_patron_by_id(self, patron_id):
    for patron in self.patrons:
      if patron.patron_id == patron_id:
        return patron
      else:
        return print(f"The patron with {patron_id} is not in the library system")
    
  def __str__(self):
    book_list = '\n '.join(str(book) for book in self.books)
    patron_list = '\n '.join(str(patron) for patron in self.patrons)
    return f" Library details: \n \n {patron_list} \n\n {book_list}"
  

if __name__ == "__main__":  
  mySweetLibrary = Library()

  book1 = book("The Silent Patient", "Alex M", "1426")
  book2 = book("Ishmael", "Daniel", "0007")

  mySweetLibrary.add_book(book1)
  mySweetLibrary.add_book(book2)

  patron1 = patron("Parth Sharma", "805587359")

  mySweetLibrary.add_patron(patron1)

  patron1.check_out_book(book1)
  patron1.check_out_book(book2)
  print(mySweetLibrary)
  
  
  patron1.return_book(book1)
  print(mySweetLibrary)
  

