
from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    email = Column(String)
    address = Column(String(200))
    fk_bank_id = Column(Integer, ForeignKey('bank.id'), nullable=False)
    bank = relationship('Bank', lazy='select', back_populates='cust_list')
    accounts = relationship('Account', lazy='select', back_populates='customer')

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __repr__(self):
        return f'Cust[{self.id}, {self.name}]'

class Account(Base):
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True, autoincrement=True)
    balance = Column(Float)
    yearly_interest_rate = Column(Float)
    fk_bank_id = Column(Integer, ForeignKey('bank.id'), nullable=False)
    bank = relationship('Bank', lazy='select', back_populates='acc_list')
    fk_customer_id = Column(Integer, ForeignKey('customer.id'), nullable=False)
    customer = relationship('Customer', lazy='select', back_populates='accounts')

    def __init__(self, customer):
        self.customer = customer
        self.balance = 0

    def deposit(self, amount):
        # TODO - as part of the home assignment please extend this method
        if amount > 0:
            self.balance += amount
        else:
            #print('amount cannot be negative')
            raise BankException('amount cannot be negative')

    def withdraw(self, amount):
        if amount < 0:
            raise InvalidAmountException('amount cannot be negative')
        if self.balance < amount:
            raise InsufficientFundsException('Insufficient funds, available', self.balance, amount)
        self.balance -= amount

    def __repr__(self):
        return f'Ac[{self.id}, {self.customer.name}, {self.balance}]'


class Bank(Base):
    __tablename__ = 'bank'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    cust_list = relationship('Customer', lazy='select', back_populates='bank')
    acc_list = relationship('Account', lazy='select', back_populates='bank')


    def __init__(self, name):
        self.name = name
        self.acc_list = []
        self.cust_list = []

    def create_customer(self, name, address):
        customer = Customer(name, address)
        customer.fk_bank_id = self.id # Assign customer to bank
        self.cust_list.append(customer)
        return customer

    def create_account(self, customer):
        account = Account(customer) # Assign account to bank
        account.fk_bank_id = self.id
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

class InsufficientFundsException(BankException):
    def __init__(self, description, amount_available, amount_requested):
        super().__init__(description)
        self.amount_available = amount_available
        self.amount_requested = amount_requested

class InvalidAmountException(BankException):
    pass



class DBSession:
    current_db_session = None

    def engine(self):
        url = 'sqlite:///data/bank.db'
        return create_engine(url, echo=True)


    def session(self):
        if not DBSession.current_db_session:
            Session = sessionmaker(bind=self.engine(), autocommit=False, autoflush=False)
            current_db_session = Session()
        return current_db_session

def init_db():
    db_session = DBSession()
    Base.metadata.create_all(db_session.engine())

