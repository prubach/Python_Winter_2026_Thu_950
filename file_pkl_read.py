import pickle
import os

if __name__ == '__main__':
    my_pkl_file = os.path.join('data', 'rates.pkl')
    with open(my_pkl_file, 'rb') as f:
        dict_rates = pickle.load(f)
        print(dict_rates)
        for k, v in dict_rates.items():
            print(k, v)
            print(type(v))