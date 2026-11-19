from bank_model import Bank

bank = Bank('SGH Bank')
c1 = bank.create_customer("John", "Warsaw")
c2 = bank.create_customer("Anne", "Cracow")
a1 = bank.create_account(c1)
a1.deposit(100)
a2 = bank.create_account(c2)
print(bank)