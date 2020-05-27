n,m=map(int,input().split())
count=0
for i in range(n):
    temp=int(input())
    if(temp%m==0):
        count+=1
print(count)
