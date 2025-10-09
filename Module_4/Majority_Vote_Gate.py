n = int(input())

count_yes = 0 
count_no = 0 

for i in range (n):
    vote = input()
    if (vote == "YES"):
        count_yes +=1
    if(vote == "NO"):
        count_no +=1

if count_yes >= count_no :
    print("ACCEPT")
else:
    print("REJECT")