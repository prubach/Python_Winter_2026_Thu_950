from bank import Customer, Account, Bank, BankException, InsufficientFundsException, InvalidAmountException

bank = Bank('SGH Bank')
c1 = bank.create_customer("John", "Warsaw")
c2 = bank.create_customer("Anne", "Cracow")
a1 = bank.create_account(c1)
a1.deposit(100)
a2 = bank.create_account(c2)
print(bank)
try:
    #a2.deposit(-300)
    # a = 26236
    # b = '52235'
    # c = a + b
    print(f'You have: {a1.balance}')
    withdraw_am = float(input('How much to withdraw: '))
    a1.withdraw(withdraw_am)
    print('after deposit and withdraw')
    print(bank)
# except (InsufficientFundsException, InvalidAmountException) as e:
#     if type(e) == InsufficientFundsException:
#         req_am = e.amount_requested
#         avail_am = e.amount_available
#         print(e, f'Requested/Available: {req_am}/{avail_am}')
#     else:
#         print(e)
except InsufficientFundsException as e:
    req_am = e.amount_requested
    avail_am = e.amount_available
    print(e, f'Requested/Available: {req_am}/{avail_am}')
except InvalidAmountException as b:
    print(b)
except Exception as e:  # This works but be careful when using it as all bugs will also be caught!!!
    print(e)
print(bank)
