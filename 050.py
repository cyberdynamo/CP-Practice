test=int(input())
for _ in range(test):
    n=int(input())
    last=n
    count=1
    while(last!=1):
    	count+=1
        if(last%2==0):
            last=last//2
        else:
            last=3*last+1
    print(count-1)
