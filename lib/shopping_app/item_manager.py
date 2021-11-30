from item import Item
from tabulate import tabulate
from itertools import groupby

def items(self): # 自身の所有する（自身がオーナーとなっている）全てのItemインスタンスを返します。
    items = []
    for item in Item.item_all():
        if item.owner == self:
            items.append(item)
    return items

def pick_items(self, number, quantity):
    items = filter(lambda num: num["number"] == number, _stock(self))
    items = list(items)[0]["items"]
    if items == None or len(items) < quantity:
        return []
    else:
        return items[0:quantity]

def items_list(self):
    table_data = []
    for stock in _stock(self):
        table_data.append([stock['number'], stock['label']['name'], stock['label']['price'], len(stock['items'])])
    print(tabulate(table_data, headers=["番号", "商品名", "金額", "数量"], tablefmt="grid"))

def _stock(self):
    if str(type(self)) != "<class 'cart.Cart'>":
        item_list = items(self)
    else:
        item_list = self.cart_items()
    item_list.sort(key=lambda m: m.name)
    group_list = []
    for key, group in groupby(item_list, key=lambda m: m.name):
        group_list.append(list(group))
    stock = []
    for i, x in enumerate(group_list):
        stock.append({"number": i, "label": {"name": x[0].name, "price": x[0].price}, "items": x})
    return stock
