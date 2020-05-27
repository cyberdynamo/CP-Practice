import math
test=int(input())
def lcm(x, y, counter=1):
    if (counter%x == 0 and counter%y == 0):
        return counter
    return lcm(x, y, counter+1)

for _ in range(test):
    a,b=map(int,input().split())
    print(math.gcd(a,b),lcm(a,b))
