class Booklist():
    def __init__(self):
        self.books = []
        
    def add(self, title, author):
        book={}
        book['title'] = title
        book['author'] = author
        self.books.append(book)   
	
    def count_books(self):
        num_books = len(self.books)
        return num_books
        

    def remove_title(self, title):
          for book in self.books:
            if title == book['title']:
                self.books.remove(book)
            
            

    def display_titles(self):
