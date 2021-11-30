from ownable import Ownable

class Item:
    instances = []

    def __init__(self, name, price, owner=None):
        self.name = name
        self.price = price
        self.owner = owner
        # Itemインスタンスの生成時、そのItemインスタンス(self)は、@@insntancesというクラス変数に格納されます。
        Item.instances.append(self)

    def label(self):
        return {"name": self.name, "price": self.price}

    @staticmethod
    def item_all():
        return Item.instances
