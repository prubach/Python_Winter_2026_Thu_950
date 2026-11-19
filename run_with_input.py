from bank import Bank
import sys

print(sys.argv)

bank_name = 'Default Bank'
if len(sys.argv) > 1:
    bank_name = sys.argv[1]

#
bank = Bank(bank_name)
c1 = bank.create_customer("John", "Warsaw")
c2 = bank.create_customer("Anne", "Cracow")
a1 = bank.create_account(c1)
a1.deposit(100)
a2 = bank.create_account(c2)
print(bank)
