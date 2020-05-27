n=int(input())
lst=list(map(int,input().split()))
flag=0
for i in range(len(lst)):
    if(lst[i]==1):
        flag=1
        break
if(flag==1):
    print("HARD")
else:
    print("EASY")
