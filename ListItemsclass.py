from operator import itemgetter
class Item:
    def __init__(self, name, price, availability):
        self.name = name
        self.price = int(price)
        self.availability = bool(availability)    

jacket = Item("jacket", 49.99, True)
cottonshirt = Item("cotton shirt", 29.99, True)
shirt = Item("shirt", 39.99, True)
trousers = Item("trousers", 59.99, True)
dress = Item("dress", 79.99, True)
blackdress = Item("black dress", 79.99, True)
# to powinno pojawi sie na github
# to też powinno być na githubie
class ItemsList:
    def __init__(self):
        self.ItemList = [jacket.__dict__, cottonshirt.__dict__, shirt.__dict__,trousers.__dict__, blackdress.__dict__, dress.__dict__]
    def displaysorted(self):
        s = itemgetter('name')
        self.ItemList.sort(key = s)
        print(self.ItemList)
Items = ItemsList()
Items.displaysorted()




