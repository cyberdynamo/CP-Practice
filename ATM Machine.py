test=int(input())
for t in range(test):
    n,k=map(int,input().split())
    lst=list(map(int,input().split()))
    str1=""
    for i in lst:
        if(k-i>=0):
            str1+="1"
            k-=i
        else:
            str1+="0"
            
    print(str1)
