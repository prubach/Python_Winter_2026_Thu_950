for i in range(10):
    print(f'{i}', end=' ')
    #print(f'i={i}')

print('\n' + '-'*60)

for i in range(3, 10):
    print(f'{i}', end=' ')
    #print(f'i={i}')

print('\n' + '-'*60)

for i in range(-20, 10, 3):
    print(f'{i}', end=' ')
    #print(f'i={i}')

print('\n' + '-'*60)

for i in reversed(range(3, 10)):
    print(f'{i}', end=' ')
    #print(f'i={i}')

print('\n' + '-'*60)

for i in range(10, 3, -1):
    print(f'{i}', end=' ')
    #print(f'i={i}')

print('\n' + '-'*60)
print('\n' + '-'*60)

for i in range(20, 50, 2):
    if i % 3 == 0:
        print('?', end=' ')
        continue
        #print(f'{i}', end=' ')
    if i > 38:
        break
    print(f'{i}', end=' ')

print('\n' + '-'*60)

i = 0
while i < 10:
    print(f'{i}', end=' ')
    i += 1

print('\n' + '-'*60)

