class Users:

    def __init__(self, unique_id, first_name, last_name, username, password, employee):
        self.unique_id = unique_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.employee = employee

    def __repr__(self):
        return "User(s): ({}, '{}', '{}', '{}', '{}', '{}')".format(self.unique_id, self.first_name, self.last_name,
                                                              self.username, self.password, self.employee)