a,b=0,0
for i in range(5):
    lst=list(map(int,input().split()))
    for j in range(5):
        if(lst[j]==1):
            a=i+1
            b=j+1
print(abs(a-3)+abs(b-3))
