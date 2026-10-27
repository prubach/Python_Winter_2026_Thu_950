
def sum_it(a=5, b=10):
    d_i = 100
    print(f'inside sum_it: {c_i}')
    return a + b

#print(sum_it(1, 5))
#print(sum_it(1))
#print(sum_it())
#print(sum_it(b=20))

c_i = 100
a_i = 11
#b_i = 0
if a_i > 10:
    b_i = 5
    c_i += 1
#else:
#    b_i = 10

for i in range(3):
    c_i += 1
    b_i += 1
print(f'a_i={a_i}, b_i={b_i}, c_i={c_i}')

e_i = sum_it(a_i, b_i)
print(f'd_i={d_i}, e_i={e_i}')

