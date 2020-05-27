def MyFunction():
    n=int(input())
    lst=list(map(int,input().split()))
    for k in range(len(lst)):
        if(lst[k]==1):
            break
        
    count=0  
    for j in range(k+1,len(lst)):
        if(lst[j]==0):
            count+=1
        else:
            if(count<5):
                return"NO"
            count=0
    return "YES"

test=int(input())
for i in range(test):
    string=MyFunction()
    print(string)
