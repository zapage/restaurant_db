class Employee:

    def __init__(self, unique_id, first_name, last_name, discount,  username, password):
        self.unique_id = unique_id
        self.first_name = first_name
        self.last_name = last_name
        self.discount = discount
        self.username = username
        self.password = password

    def __repr__(self):
        return "Employee(s): ({}, '{}', '{}', {}, '{}', '{}')".format(self.unique_id, self.first_name,
                                                          self.last_name, self.discount, self.username, self.password)