class Beverages:

    def __init__(self, item_id, item_name, alcoholic, price, quantity):
        self.item_id = item_id
        self.item_name = item_name
        self.alcoholic = alcoholic
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return "Beverage(s): ({}, '{}', '{}', {}, {})".format(self.item_id, self.item_name, self.alcoholic,
                                                          self.price, self.quantity)