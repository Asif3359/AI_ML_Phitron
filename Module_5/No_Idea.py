n, m = map(int, input().split())
lst = list(map(int, input().split()))

A = set(map(int, input().split()))
B = set(map(int, input().split()))

ans = 0

for num in lst:
    if num in A:
        ans += 1
    elif num in B:
        ans -= 1

print(ans)
