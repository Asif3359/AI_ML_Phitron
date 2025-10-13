n = int(input())
lst1 = list(map(int , input().split()))
lst2 = list(map(int , input().split()))

lst = lst2+lst1

print(*lst)