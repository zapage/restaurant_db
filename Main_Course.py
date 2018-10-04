class MainCourse:

    def __init__(self, item_id, item_name, quantity, price,):
        self.item_id = item_id
        self.item_name= item_name
        self.quantity = quantity
        self.price = price

    def __repr__(self):
        return "Main Course(s): ({}, '{}', {}, {})".format(self.item_id, self.item_name,
                                                          self.quantity, self.price)