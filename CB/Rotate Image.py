n=int(input())
lst=[]
for i in range(n):
    tmplst=list(map(int,input().split()))
    lst.append(tmplst)

for i in range(n-1,-1,-1):
    for j in range(n):
        print(lst[j][i],end=" ")
    print()
