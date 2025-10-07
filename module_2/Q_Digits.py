t = int(input())

for _ in range(t):
    n = int(input())

    if n == 0:
        print(0)
        continue

    digits = []

    while n > 0:
        digits.append(n % 10)
        n //= 10

    print(*digits)
