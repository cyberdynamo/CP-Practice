n,k=map(int,input().split())
lst=list(map(int,input().split()))
k=lst[k-1]
count=0
for i in range(len(lst)):
    if(lst[i]>=k and lst[i]>0):
        count+=1
print(count)
