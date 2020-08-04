def PrintList(array):
    for i in array:
        print(i,end=" ")
    print()

def countOdd(lst):
    count=0
    n=len(lst)
    for i in range(n):
        s=0
        for j in range(i,n):
            s+=lst[j]
            if(s%2!=0):
                PrintList(lst[i:j+1])
                count+=1
    if(count==0):
        print("-1")

lst=list(map(int,input().split()))
countOdd(lst)
