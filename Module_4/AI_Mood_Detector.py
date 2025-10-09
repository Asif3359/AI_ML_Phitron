st = input()

happy=st.__contains__("happy")
joy=st.__contains__("joy")
smile=st.__contains__("smile")


sad=st.__contains__("sad")
cry=st.__contains__("cry")
angry=st.__contains__("angry")

if happy or joy or smile :
    print("Happy Mood")
elif sad or cry or angry :
    print("Sad Mood")
else:
    print("Neutral Mood")

