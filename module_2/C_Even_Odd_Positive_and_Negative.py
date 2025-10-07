A = int(input())
numbers = list(map(int, input().split()))

Even = 0
Odd = 0
Positive = 0
Negative = 0

for x in numbers:
    if x > 0:
        Positive += 1
    elif x < 0:
        Negative += 1

    if x % 2 == 0:
        Even += 1
    else:
        Odd += 1

print("Even:", Even)
print("Odd:", Odd)
print("Positive:", Positive)
print("Negative:", Negative)
