class Cart:
    from item_manager import items, items_list
    from ownable import Ownable

    def __init__(self, owner):
        self.owner = owner
        self.items = []

    def cart_items(self):
        return self.items

    def add(self, item):
        self.items.append(item)

    def total_amount(self):
        price_list = []
        for item in self.items:
            price_list.append(item.price)
        return sum(price_list)

    def check_out(self):
        if self.owner.wallet.balance < self.total_amount():
            return
        for item in self.cart_items():
            item.owner.wallet.deposit(self.owner.wallet.withdraw(item.price))
            item.owner = self.owner
        self.items.clear()
