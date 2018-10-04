class BillingInformation:

    def __init__(self, first_name, last_name, address, phone, zip_code, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone = phone
        self.zip_code = zip_code
        self.email = email

    def __repr__(self):
        return "Billing Information: ('{}', '{}', '{}', '{}', {}, '{}')".format(self.first_name, self.last_name,
                                                          self.address, self.phone, self.zip_code, self.email)