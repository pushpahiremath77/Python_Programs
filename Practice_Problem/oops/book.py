# Basic Class with Methods: Create a class Book with attributes title, author, and price. Add methods to:

# Display book details.
# Apply a discount to the price.


class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price

    def display(self):
        print(f"Title is :{self.title} \nAuthor is :{self.author} \nPrice is :{self.price}")

    def get_discount(self,discount):
        after_discount = self.price-(self.price*discount)//100
        print(f"After discount : {after_discount}")


book1 = Book("DevOps","Disha",10000)
book1.display()
book1.get_discount(50)
