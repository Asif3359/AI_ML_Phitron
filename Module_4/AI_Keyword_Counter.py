message = input().split()


total = message.count("ai") + message.count("data")+message.count("model")+message.count("learn")+message.count("train")+message.count("neural")

if total>=2 :
    print("AI Detected")
else:
    print("Not AI Related")