import math
def Fib(n):
    return round((((1+math.sqrt(5))/2)**n)/(math.sqrt(5)))

n=int(input())
for i in range(n+1):
    print(Fib(i),end=" ")
