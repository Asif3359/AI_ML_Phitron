n = int(input())
target = float(input())
sum = 0 

for i in range(n):
    x = float(input())
    sum += x

avg = sum/n 

if avg <= target:
    print("PASS")
else:
    print("RETRY")