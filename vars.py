print('Hello world')
a = 10
type_a = type(a)
print(f'a={a}')
print(f'type_a={type_a}')
b = 354
c = a + b
print(f'c={c}')
d = a * b
print(f'd={d}')
e = 141.45435
print(f'e={e}')
print(f'type(e)={type(e)}')
f = 15435.41413
g = e + f
print(f'g={g}')
s = 'hello world'
print(f's={s}')
print(f'type(s)={type(s)}')
s_a = '525'
print(f's_a={s_a}')
s_b = '823'
#s_c = int(s_a) + int(s_b)
'''
Multiline comment

'''
s_c = s_a + s_b
print(f's_c={s_c}')
print(f'type(s_c)={type(s_c)}')
i_c = int(s_c)
print(f'type(i_c)={type(i_c)}')
i_c = i_c + 100
print(f'i_c={i_c}')

s_d = str(i_c) + '0000'
print(f's_d={s_d}')

#print(f'type(s)={type(s)}')

f_a = 52525.25235
s_fa = str(f_a)
print(f's_fa={s_fa}')
print(f'type(s_fa)={type(s_fa)}')

s_fa += '123'
print(f's_fa={s_fa}')
f_b = float(s_fa)
print(f'f_b={f_b}')
#i_a = 553


print('---------------------------------------')
i_a = 453632672369108790217593275903725908123750912650659635093605973259273509237902376026
i_b = 376938790123760912756026509259591725987259256210521095872750921875892719507129572597
i_c = i_a + i_b
n_dig = len(str(i_c))
print(f'i_c={i_c}')
print(f'n_dig={n_dig}')

f_a = 453632672369108790217593275903725908123750912650659635093605973259273509237902376026.0
f_b = 376938790123760912756026509259591725987259256210521095872750921875892719507129572597.0
print(f'type(f_a)={type(f_a)}')
print(f'f_a={f_a}')
print(f'f_b={f_b}')
f_c = f_a + f_b
print(f'f_c={f_c}')

bi_a = 0b1011
print(f'bi_a={bi_a}')
xi_a = 0x1f
print(f'xi_a={xi_a}')
import sys
print(sys.float_info)