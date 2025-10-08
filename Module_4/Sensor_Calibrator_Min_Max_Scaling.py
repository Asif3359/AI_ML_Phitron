n1, n2, n3 = input().split()
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)


norm = (n1 - n2)/(n3-n2)
print(f"{norm:.2f}")