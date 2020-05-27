n=int(input())
lst=list(map(int,input().split()))
newlst=[1]*n
for i in range(n):
    newlst[lst[i]-1]=i+1
for j in range(n):
    print(newlst[j],end=" ")
