string=input()
rev=string[::-1]
count=0
for i in range(len(string)):
    if(string[i]==rev[i]):
        count=count+1
    else:
        break
if(count!=0):
    print(string[:count+1])
else:
    print("-1")
