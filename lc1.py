#Programmer: Kritansh Mehrotra    Contest: CC April COOKOFF
#Time: 09:30 PM
#Date: 20/04/2020

test=int(input())
for t in range(test):
    size,n=map(int,input().split())
    mul=n*n
    factor=n*n
    s=0
    for i in range(2,size+1):
        for j in range(1,2*i-1):
            mul=mul*factor
        s+=mul
        factor=mul*factor
        mul=factor
    s=s+n
    print(s%(10**9+7))

        
            
            
            
        
        
    
