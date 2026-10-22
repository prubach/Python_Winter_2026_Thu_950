list_a = [3, 5, 7, 9, 11, 13, 15]
print(list_a)

list_a.append(11)
print(list_a)

list_a.insert(1, 4)
print(list_a)

# Remove by value - removes first occurence
list_a.remove(11)
print(list_a)

list_a.remove(11)
print(list_a)

# Remove by index
list_a.pop(3)
print(list_a)

list_b = list(reversed(list_a))
print(list_b)

list_b.sort()
print(list_b)
