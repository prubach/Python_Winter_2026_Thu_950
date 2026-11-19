from bank import Customer, Account, Bank, BankException, InsufficientFundsException

bank = Bank('SGH Bank')
c1 = bank.create_customer("John", "Warsaw")
c2 = bank.create_customer("Anne", "Cracow")
a1 = bank.create_account(c1)
a1.deposit(100)
a2 = bank.create_account(c2)
print(bank)
try:
    #a2.deposit(-300)
    print(f'You have: {a1.balance}')
    withdraw_am = float(input('How much to withdraw: '))
    a1.withdraw(withdraw_am)
    print('after deposit and withdraw')
    print(bank)
except BankException as b:
    print(b)
except InsufficientFundsException as e:
    req_am = e.amount_requested
    avail_am = e.amount_available
    print(e, f'Requested/Available: {req_am}/{avail_am}')
