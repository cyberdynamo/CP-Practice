num=int(input())
lst=list(map(int,input().split()))
for i in range(len(lst)):
    if(lst[i]%2==0):
        lst[i]=lst[i]-1
for i in lst:
    print(i,end=" ")
