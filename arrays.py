a_a = [3, 5, 7, 9, 11]
print(a_a)
print(type(a_a))
print(a_a[2])
print('length of a_a = ' + str(len(a_a)))
print('length of a_a = {}'.format(len(a_a)))
print(f'length of a_a = {len(a_a)}')
a_b = a_a[1:]
print(a_b)
a_b = a_a[1:3]
print(a_b)
a_b = a_a[:3]
print(a_b)
a_b = a_a[-2:]
print(a_b)
print('-------------------')

i_s = 0
for a in a_a:
    i_s += a
    print(a)
print(a)
print(f'i_s={i_s}')