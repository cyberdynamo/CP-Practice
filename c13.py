test=int(input())
for i in range(test):
    num=int(input())
    rev=0
    while(num!=0):
        d=num%10
        rev=rev*10+d
        num//=10
    print(rev)
