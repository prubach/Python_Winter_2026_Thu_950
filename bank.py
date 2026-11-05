
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
    yearly_interest_rate = 0.02  # TODO - will be used to update the interest rate

    def __init__(self, customer):
        self.customer = customer
        Account.last_id += 1
        self.id = Account.last_id
        self.balance = 0

    def deposit(self, amount):
        # TODO - as part of the home assignment please extend this method
        if amount > 0:
            self.balance += amount
        else:
            #print('amount cannot be negative')
            raise BankException('amount cannot be negative')

    def withdraw(self, amount):
        # TODO - as part of the home assignment please extend this method
        self.balance -= amount

    def __repr__(self):
        return f'Ac[{self.id}, {self.customer.name}, {self.balance}]'


class Bank:
    def __init__(self, name):
        self.name = name
        self.acc_list = []
        self.cust_list = []

    def create_customer(self, name, address):
        customer = Customer(name, address)
        self.cust_list.append(customer)
        return customer

    def create_account(self, customer):
        account = Account(customer)
        self.acc_list.append(account)
        return account

    def transfer_money(self, from_account_id, to_account_id, amount):
        # TODO - as part of the home assignment please implement this method - as names suggest the input parameters are
        # ids of the accounts to transfer money from and to and amount to transfer. You may need a helper method to find
        # those accounts based on their ids.
        pass

    def run_daily_interest_updater(self):
        # TODO - as part of the home assignment please implement this method
        pass

    def __repr__(self):
        return f'Bank[{self.name}, {self.cust_list}, {self.acc_list}]'

class BankException(Exception):
    pass

#TODO
# Add deposit and withdraw (charge) methods and code that will demonstrate their use