test=int(input())
for t in range(test):
    n,k=map(int,input().split())
    tmp=n//k
    lst=[]
    j=k
    q=1
    for i in range(tmp):
        j*=q
        lst.append(j)
        q+=1

print(lst[555])
    
