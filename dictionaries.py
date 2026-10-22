dict_a = {'PLN': 1, 'USD': 3.7, 'EUR': 4.3}
print(dict_a)
print(dict_a['USD'])
print(dict_a.get('USD'))
print(dict_a.get('GBP'))
#print(dict_a['GBP'])
print(dict_a.get('GBP', 5.5))