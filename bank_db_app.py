from bank_model import Bank, init_db, DBSession, Customer

db = DBSession().session()

def add_data():
    init_db()
    bank = Bank('SGH Bank')
    db.add(bank)
    c1 = bank.create_customer("John", "Warsaw")
    c2 = bank.create_customer("Anne", "Cracow")
    db.add(c1)
    db.add(c2)
    a1 = bank.create_account(c1)
    db.add(a1)
    a1.deposit(100)
    a2 = bank.create_account(c2)
    db.add(a2)
    print(bank)
    db.commit()


def get_customer():
    customers = db.query(Customer).all()
    for c in customers:
        print(c)
        c.email = 'myemail@sgh'
        #db.save(c)
        print(c.accounts)
    db.commit()


get_customer()