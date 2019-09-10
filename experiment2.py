a = 1
b = 1

for i in range(10):
    print(a, end=' ')
    c = a
    a = b
    b = a + c
print()