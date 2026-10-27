my_file=('data\\rates.csv')

def read_rates_csv(my_file):
    f=open(my_file)

    next(f)
    dict_a = {}
    for line in f.readlines():
        z=line.split(',')
        dict_a[z[0]] = float(z[1])
    return dict_a


if __name__ == '__main__':
    dict_a = read_rates_csv(my_file)

    print(dict_a)
    for k, v in dict_a.items():
        print(k, v)
        print(type(k), type(v))