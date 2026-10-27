import json
import os
from read_csv_rates import read_rates_csv

if __name__ == '__main__':
    my_file= 'data\\rates.csv'
    my_json_file = os.path.join('data', 'rates.json')

    dict_rates = read_rates_csv(my_file)
    print(dict_rates)

    with open(my_json_file, 'w') as outfile:
        json.dump(dict_rates, outfile)
