class Item: 
    def __init__(self,category,name,price):
        self.category = category
        self.name = name
        self.price = price
    count = 0

class Shopping:
    def __init__(self):
        self.cart_items = []

    def add_items(self,item):
        self.cart_items.append(item)
        Item.count+=1
        return Item.count

        
item = Item("Shoes","nike",1000)
print(item.name)
cart1 = Shopping()
cart1.add_items(item)













        