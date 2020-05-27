test=int(input())
for i in range(test):
    num=int(input())
    num1=num%10
    str1=str(num)
    l=len(str1)
    for j in range(l-1):
        num=num//10
    print(num1+num)
