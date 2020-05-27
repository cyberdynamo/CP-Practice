n,h=map(int,input().split())
lst=list(map(int,input().split()))
count=0
for i in range(len(lst)):
    if(lst[i]>h):
        count+=1
print(n+count)
