#Pascal Triangle
n=int(input())
arr=[[None]*n for _ in range(n)]
arr[0][0]=1

if(n==1):
    print(1)
else:
    for i in range(1,n):
        arr[i][0]=1
        arr[i][i]=1
        
        for j in range(1,i):
            arr[i][j]=arr[i-1][j-1]+arr[i-1][j]

for i in range(n):
    for k in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print(arr[i][j],end=" ")
    print()
