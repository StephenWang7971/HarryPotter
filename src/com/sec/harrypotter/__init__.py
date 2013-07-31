
def get_discount_rate(items):
    if len(items) == 5:
        return 0.75;
    if len(items) ==  4:
        return 0.8;
    if len(items) ==  3:
        return 0.9;
    if len(items) == 2:
        return 0.95;
    return 1.0;

class Book:
    index = "#0";
    name = "";
    price = 8;
    def __init__(self, index, name, price):
        self.index = index;
        self.name = name
        self.price = price

class Item:
    def __init__(self, book, count):
        self.book = book
        self.count = count
        
    book = Book,
    count = 0;

class Cart:
    items = []
    def add_item(self, item):
        self.items.append(item);

def pick_most_books(cart):
    items = [];
    for i in range(0, len(cart.items)):
        item = cart.items[i];
        if item.count == 0:
            continue;
        items.append(Item(item.book, 1));
        cart.items[i].count -= 1;
    return items;

def is_empty(cart):
    for item in cart.items:
        if item.count > 0:
            return False;
    return True;

def find_best_solution(cart):
    strategies = [];
    price = 0.0;
    while not is_empty(cart):
        items = pick_most_books(cart);
        strategies.append(items);
        rate = get_discount_rate(items);
        price += 8 * len(items) * rate;
    return price;

if __name__ == '__main__':
    item_1 = Item(Book("#1.", "Philosophy Stone", 8), 2);
    item_2 = Item(Book("#2.", "Secret Chamber", 8), 2);
    item_3 = Item(Book("#3.", "Prisoner of Azkaban", 8), 2);
    item_4 = Item(Book("#4.", "Goblet of Fire", 8), 1);
    item_5 = Item(Book("#5.", "The Order of Phoenix", 8), 1);
    
    cart = Cart();
    cart.add_item(item_1);
    cart.add_item(item_2);
    cart.add_item(item_3);
    cart.add_item(item_4);
    cart.add_item(item_5);
    
    price = find_best_solution(cart);
    '''replace 5-3 with 4-4 strategies'''
    '''count_price(strategies)'''
    print(price);