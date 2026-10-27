import pickle
import os
from read_csv_rates import read_rates_csv

if __name__ == '__main__':
    my_file= 'data\\rates.csv'
    my_pkl_file = os.path.join('data', 'rates.pkl')

    dict_rates = read_rates_csv(my_file)
    print(dict_rates)

    with open(my_pkl_file, 'wb') as outfile:
        pickle.dump(dict_rates, outfile)
