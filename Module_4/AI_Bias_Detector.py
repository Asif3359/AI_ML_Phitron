lst = input().split()

count_A = lst.count("A")
count_B = lst.count("B")

total = len(lst)

A = (count_A / total) * 100
B = (count_B / total) * 100

if (A > 70) or (B > 70) :
    print("Biased Model")
else:
    print("Fair Model")