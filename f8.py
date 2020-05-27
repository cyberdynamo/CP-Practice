n=int(input())
c=0
for i in range(n):
    string=input()
    if(string=="X++" or string=="++X"):
        c+=1
    elif(string=="X--" or string=="--X"):
        c-=1
print(c)
