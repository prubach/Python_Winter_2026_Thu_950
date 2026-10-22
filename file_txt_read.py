import os
my_file = 'data/hello.txt'
my_file = 'data\\hello.txt'
my_file = os.path.join('data', 'hello.txt')

f = open(my_file)
for line in f.readlines():
    print(line)
f.close()