test=int(input())
for _ in range(test):
    quant,price=map(int,input().split())
    if(quant>1000):
        total=(quant*price)-((quant*price)*0.1)
        print("{:0.6f}".format(total))
    else:
        total=quant*price
        print("{:0.6f}".format(total))
