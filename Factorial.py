test=int(input())
for t in range(test):
    n=int(input())
    count=0
    f=5
    while(n>=5):
        n=n//5
        f=f*5
        count+=n
    print(count)
