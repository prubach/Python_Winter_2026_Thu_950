import json
import os

if __name__ == '__main__':
    my_json_file = os.path.join('data', 'rates.json')
    with open(my_json_file) as f:
        dict_rates = json.load(f)
        print(dict_rates)
        for k, v in dict_rates.items():
            print(k, v)
            print(type(v))