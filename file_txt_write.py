import os
my_file = 'data/hello.txt'
my_file = 'data\\hello.txt'
my_file = os.path.join('data', 'hello_out.txt')

with open(my_file, 'a') as f:
    f.write('hello')
    f.write(' Python')
    f.write('\n')
    f.write('Abcd')
