x = int(input())
numbers = input()

numbers_int = [int(x) for x in numbers.split()]

Min = min(numbers_int)

print(Min , numbers_int.index(Min)+1)

