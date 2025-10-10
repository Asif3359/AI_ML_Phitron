string = input()

dic = {}

for i in string:
    dic[i] = dic.get(i, 0) + 1

for k in sorted(dic.keys()):
    print(f"{k} : {dic[k]}")
