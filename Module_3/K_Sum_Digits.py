x = int(input())
n = input().strip()

total = 0
for digit in n:
    total += int(digit)

print(total)