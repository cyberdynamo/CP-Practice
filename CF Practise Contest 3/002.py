n=int(input())
lst=list(map(int,input().split()))
s=0
for i in range(n):
    s+=lst[i]
    temp=lst[i]-1
    temp2=temp*i
    s+=temp2
print(s)
