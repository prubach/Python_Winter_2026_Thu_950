p = False
q = False
print(f'p={p}, q={q}')

if p and q:
    print("p and q are True")
else:
    print("p or q are False")

print('-'*80)

if p or q:
    print("p or q are True")
else:
    print("p and q are False")


print('-'*80)

if not (p or q):
    print("not (p or q) are True")
else:
    print("p or q are True")


print('-'*80)

# XOR operation - Exclusive OR
if p ^ q:
    print("p xor q are True")
else:
    print("p xor q are False")

