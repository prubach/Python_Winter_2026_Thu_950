
class Customer:
    last_id = 0
    def __init__(self, name, address):
        self.name = name
        self.address = address
        Customer.last_id += 1
        self.id = Customer.last_id

    def __repr__(self):
        return f'Cust[{self.id}, {self.name}]'

class Account:
    last_id = 1000
    def __init__(self, customer):
        self.customer = customer
        Account.last_id += 1
        self.id = Account.last_id
        self.balance = 0

    def __repr__(self):
        return f'Ac[{self.id}, {self.customer.name}, {self.balance}]'