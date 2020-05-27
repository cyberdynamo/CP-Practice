def fact(num):
    factorial=num
    while(num!=1):
        factorial=factorial*(num-1)
        num=num-1
    return factorial

test=int(input())
for i in range(test):
    temp=int(input())
    print(fact(temp))
