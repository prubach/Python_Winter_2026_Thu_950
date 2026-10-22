import os
my_file = 'data/hello.txt'
my_file = 'data\\hello.txt'
my_file = os.path.join('data', 'hello.txt')

f = open(my_file)
for line in f.readlines():
    print(line, end='')
f.close()

print('\n' + '-'*60)

with open(my_file, mode='r') as f:
    for line in f.readlines():
        print(line, end='')
