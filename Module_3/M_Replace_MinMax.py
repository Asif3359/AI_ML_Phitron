x = int(input())
numbers = input()

numbers_int = [int(x) for x in numbers.split()]

Min = min(numbers_int)
Max = max(numbers_int)


min_index = numbers_int.index(Min)
max_index = numbers_int.index(Max)

numbers_int[min_index]=Max
numbers_int[max_index]=Min

print(*numbers_int)
