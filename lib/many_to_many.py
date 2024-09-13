class Author:
    all= []
    def __init__(self,name) -> None:
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [contract.book for contract in Contract.all if contract.author == self]
    
    def sign_contract(self,book, date, royalties):
        return Contract(self,book, date, royalties)
    
    def total_royalties(self):
        return sum([contract.royalties for contract in Contract.all if contract.author == self])


class Book:
    all= []
    def __init__(self,title) -> None:
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self]


class Contract:
    all= []
    def __init__(self,author,book,date,royalties) -> None:
       self.author = author
       self.book = book
       self.date = date
       self.royalties = royalties
       Contract.all.append(self)

    @property
    def author(self):
      return self._author
    
    @author.setter
    def author(self,author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise ValueError("author should be an instance of class Author")
        
    @property
    def book(self):
      return self._book
    
    @book.setter
    def book(self,book):
        if isinstance(book, Book):
            self._book = book
        else:
            raise ValueError("book should be an instance of class Book")

    @property
    def date(self):
      return self._date
    
    @date.setter
    def date(self,date):
        if isinstance(date, str):
            self._date = date
        else:
            raise ValueError("date should be a string")

    @property
    def royalties(self):
      return self._royalties
    
    @royalties.setter
    def royalties(self,royalties):
        if isinstance(royalties, int):
            self._royalties = royalties
        else:
            raise ValueError("royalties should be an integer")
        
    @classmethod
    def contracts_by_date(cls, date): 
        return [contract for contract in cls.all if contract.date == date]
   
    