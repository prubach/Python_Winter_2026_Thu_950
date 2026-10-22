dict_a = {'PLN': 1, 'USD': 3.7, 'EUR': 4.3}
print(dict_a)
print(dict_a['USD'])
print(dict_a.get('USD'))
print(dict_a.get('GBP'))
#print(dict_a['GBP'])
print(dict_a.get('GBP', 5.5))

print('-'*60)

print(dict_a.keys())
print(list(dict_a.keys()))

for key in dict_a.keys():
    print(f'key={key}, value={dict_a.get(key)}')

print('-'*60)
print(dict_a.values())
print(type(dict_a.values()))
print(list(dict_a.values()))

print('-'*60)

for key, value in dict_a.items():
    print(f'key={key}, value={value}')