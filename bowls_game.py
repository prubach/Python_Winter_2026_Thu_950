'''
 * * * * *
  * * * *
   * * *
    * *
     *

n - number of rows of bowls - here n=5
'''

def count_bowls(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
    #...
    return

def count_bowls_list(n):
    x = list()
    for i in range(1, n+1):
        x.append(i)
    return(sum(x))


def count_bowls_recursive(n):
    if n > 0:
        result = n + count_bowls_recursive(n - 1)
    else:
        result = 0
    return result

def count_bowls_sequence(n):
    return round(n * (n + 1) / 2)

#def count_bowls_sequence(n):
n = 997

#print(f'count_bowls({n})={count_bowls(n)}')
#print(f'count_bowls_list({n})={count_bowls_list(n)}')
#print(f'count_bowls_recursive({n})={count_bowls_recursive(n)}')

from performance_tests import *
#from performance_tests import time_func

time_func(count_bowls, n)
time_func(count_bowls_list, n)
time_func(count_bowls_recursive, n)
time_func(count_bowls_sequence, n)