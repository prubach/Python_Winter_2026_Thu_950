from bank import Customer, Account, Bank, BankException

bank = Bank('SGH Bank')
c1 = bank.create_customer("John", "Warsaw")
c2 = bank.create_customer("Anne", "Cracow")
a1 = bank.create_account(c1)
a1.deposit(100)
a2 = bank.create_account(c2)
print(bank)
try:
    a2.deposit(-300)
    a1.withdraw(200)
    print('after deposit and withdraw')
    print(bank)
except BankException as b:
    print(b)