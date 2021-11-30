from wallet import Wallet

class User:
    from item_manager import items_list, items, pick_items, items_list

    def __init__(self, name):
        self.name = name
        self.wallet = Wallet(self)
