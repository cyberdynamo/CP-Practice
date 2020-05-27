test=int(input())
for t in range(test):
    n=int(input())
    s1=list(input().split())
    m=int(input())
    s2=list(input().split())
    f=0
    for i in range(n-m+1):
        if(s1[i:i+m]==s2):
            print("Yes")
            f=1
            break
    if(f==0):
        print("No")
    
        
