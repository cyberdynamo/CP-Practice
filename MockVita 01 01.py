import math
test=int(input())
for t in range(test):
    n=int(input())
    var=1
    count=0
    while(var<=n):
        var*=2
        count+=1
    print(count)
