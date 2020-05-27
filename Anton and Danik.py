n=int(input())
string=input()
c1,c2=0,0
for i in range(len(string)):
    if(string[i]=="A"):
        c1+=1
    else:
        c2+=1
if(c1>c2):
    print("Anton")
elif(c2>c1):
    print("Danik")
else:
    print("Friendship")
