n=int(input())
lst=list(map(int,input().split()))
count=1
maxi=0
for i in range(n-1):
    if(lst[i]<=lst[i+1]):
        count+=1
    else:
        if(count>maxi):
            maxi=count
        count=1
if(count>maxi):
    maxi=count
print(maxi)
