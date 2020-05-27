test=int(input())
def sum(n):
    s=0
    for i in range(1,n+1):
        s+=i
    return s
        
for _ in range(test):
    d,n=map(int,input().split())
    for i in range(d):
        n=sum(n)
    print(n)
    
