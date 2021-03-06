class Strategy:
    def __init__(self, items):
        self.items = items;
        self.rate = self.get_discount_rate();
   
    def get_discount_rate(self):
        if len(self.items) == 5:
            return 0.75;
        if len(self.items) ==  4:
            return 0.8;
        if len(self.items) ==  3:
            return 0.9;
        if len(self.items) == 2:
            return 0.95;
        return 1.0;

    def get_price(self):
        return self.total_price() * self.rate;

    def total_price(self):
        price = 0.0;
        for item in self.items:
            price += item.book.price;
        return price;

    def count(self):
        return len(self.items);
    

class StrategyOptimizer:
    def optimize(self, strategies):
        found = False;
        while True:
            found = self.replace_53_with_44(strategies);
            if not found:
                break;
        return strategies;

    def replace_53_with_44(self, strategies):
        strategyMap = {};
        strategyMap.clear();
        for i in range(0, len(strategies)):
            strategy = strategies[i];
            strategyMap[strategy.count()] = i;

        if (strategyMap != None and len(strategyMap) != 0):
            if (strategyMap.get(5, None) != None and strategyMap.get(3, None) != None):
                self.move_book(strategies[strategyMap[5]], strategies[strategyMap[3]]);
                return True;
        return False;

    def move_book(self, source, dest):
        item = self.findAnyDiff(source, dest);
        if item == None:
            return;
        source.items.remove(item);
        source.rate = source.get_discount_rate();
        dest.items.extend([item]);
        dest.rate = source.get_discount_rate();
        return;
    
    def findAnyDiff(self, source, dest):
        for item in source.items:
            if item not in dest.items:
                return item;
        return None;

class Book:
    def __init__(self, index, name, price):
        self.index = index;
        self.name = name
        self.price = price

class Item:
    def __init__(self, book, count):
        self.book = book
        self.count = count

class Cart:
    items = [];
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

def count_price(strategies):
    price = 0;
    for s in strategies:
        price += s.get_price();
    return price;

def find_best_solution(cart):
    strategies = [];
    price = 0.0;
    while not is_empty(cart):
        items = pick_most_books(cart);
        strategy = Strategy(items);
        strategies.append(strategy);
    return strategies;

def count_best_price(cart):
    strategies = find_best_solution(cart);
    so = StrategyOptimizer();
    strategies = so.optimize(strategies)
    price = count_price(strategies);
    print(price);

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

    count_best_price(cart);
    
