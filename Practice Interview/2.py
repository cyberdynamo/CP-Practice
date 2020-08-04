#Fibonacci Number Using Formula O(1)
import math
def Fib(n):
    a=((math.sqrt(5)+1))/2
    return int((a**n)/(math.sqrt(5)))

while(True):
    n=int(input())
    print(Fib(n))
