test=int(input())
for i in range(test):
    num=int(input())
    s=0
    while(num!=0):
        d=num%10
        s+=d
        num=num//10
    print(s)
