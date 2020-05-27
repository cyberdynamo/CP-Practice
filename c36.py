test=int(input())
for _ in range(test):
    num=int(input())
    if(num<1500):
        sal=num+(num*0.10)+(num*0.90)
    else:
        sal=num+500+((num*98)/100)
    print("{:0.2f}".format(sal))
