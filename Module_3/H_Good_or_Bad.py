x = int(input())

for i in range(x):
    numbers = input()
    if numbers.find("010") != -1 or numbers.find("101") != -1:
        print("Good")
    else:
        print("Bad")