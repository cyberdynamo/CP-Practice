lst=[2,3,4,5,6,7,8,9,10,1,11,10,10,10,2,3,4,5,6,7,8,9,10,1,11,10,10,10,2,3,4,5,6,7,8,9,10,1,11,10,10,10,2,3,4,5,6,7,8,9,10,1,11,10,10,]
n=int(input())
temp=n-10
count=0
for i in range(len(lst)):
    if(lst[i]+10==n):
        count+=1
print(count)
