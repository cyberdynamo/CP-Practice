#Programmer: Kritansh Mehrotra

test=int(input())
for t in range(test):
    n=int(input())
    lst=list(map(int,input().split()))
    count=1
    mini=999999
    maxi=0
    for i in range(1,n):
        temp=lst[i]-lst[i-1]
        if(temp<=2):
            count+=1
        else:
            if(count<mini):
                mini=count
            if(count>maxi):
                maxi=count
            count=1
    if(count<mini):
        mini=count
    if(count>maxi):
        maxi=count
    if(mini==999999):
        mini=n
    if(maxi==0):
        maxi=n
    print(mini,maxi)
