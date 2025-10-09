numbers = input().split()

total = 0 

for number in numbers :
    total = total + int(number)

avg = total/len(numbers) 

if avg < 85 :
    print("Dark Image")
elif(avg <= 170) :
    print("Normal Image")
elif(avg > 170) :
    print("Bright Image")