list_a = [3, 5, 7, 9, 11, 13, 15, 11, 15]
print(list_a)
print(type(list_a))
print(list_a[5])

tuple_a = (3, 5, 7, 9, 11, 13, 15, 11, 15)
print(tuple_a)
print(type(tuple_a))
print(tuple_a[5])
# Append, remove etc. won't work on a tuple - it is immutable
#tuple_a.append(3)
#tuple_a.remove(3)
#tuple_a[5] = 20
print(tuple_a)

set_a = set(tuple_a)
#set_a = set(list_a)
# set - unordered, no duplicates = unique values
print(set_a)
print(type(set_a))

list_c = list(set_a)
print(list_c)




