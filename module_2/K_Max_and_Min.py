A, B, C = input().split()

a = int(A)
b = int(B)
c = int(C)

min = a
max = a

if b < min:
    min = b
if c < min:
    min = c

if b > max:
    max = b
if c > max:
    max = c

print(min, max)
