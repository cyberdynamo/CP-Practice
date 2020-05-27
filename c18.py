test=int(input())
for _ in range(test):
    n=int(input())
    if(n==0):
        print("1")
    else:
        fact=n
        for i in range(n-2):
            n=n-1
            fact=fact*(n)
        print(fact)
