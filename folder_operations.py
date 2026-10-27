import os

my_folder = 'data'
my_folder = 'c:/Users/prubac/PycharmProjects/Python_Winter_2026_Thu_950/data'

#my_file = 'C:\\Users\\prubac\\Documents\\rates_a.csv'
my_file = '..\\..\\Documents\\rates_a.csv'

cwd = os.getcwd()
print(f'cwd: {cwd}') # Current working directory

with open(my_file) as file:
    file_read = file.readlines()
    print(file_read)

print('-'*60)

files = os.listdir(my_folder)
for file in files:
    print(file)