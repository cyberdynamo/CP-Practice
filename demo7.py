n=int(input())
lst2=list(map(int,input().split()))
lst=sorted(lst2)
s=sum(lst)
k=0
flag=0
for i in range(n):
    if((s-lst[i])%7==0):
        flag=1
        k=lst[i]
        break
if(flag==0):
    print(-1)
else:
    print(lst2.index(k))
        
