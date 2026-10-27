import pandas as pd

df = pd.read_csv('data/rates.csv')
print(df.head())
df = df.set_index('Currency')
print(df.head())

#rates_dict_col = df.to_dict()
#rates_dict = rates_dict_col['Rate']

rates_dict = df['Rate'].to_dict()
print(rates_dict)

for k, v in rates_dict.items():
    print(k, v)
    print(type(k), type(v))