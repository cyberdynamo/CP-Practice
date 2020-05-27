n=int(input())
lst=list(map(int,input().split()))
maxi=101
for j in range(maxi):
    for i in range(1,n):
        if(lst[i]<lst[i-1]):
            temp=lst[i-1]-lst[i]
            lst[i-1]-=temp
            lst[i]+=temp
print(*lst)
