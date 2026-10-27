my_file=('data\\rates.csv')
f=open(my_file)

next(f)
dict_a = {}
for line in f.readlines():
    z=line.split(',')
    dict_a[z[0]] = float(z[1])

print(dict_a)
for k, v in dict_a.items():
    print(k, v)
    print(type(k), type(v))