test=int(input())
def Check(n):
    while(n!=0):
        d=n%10
        if(d!=3 and d!=5):
            return False
        n=n//10
    return True

for t in range(test):
    n=int(input())
    while(True):
        n+=1
        if(Check(n)==True):
            print(n)
            break
