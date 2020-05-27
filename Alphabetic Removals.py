n,k=map(int,input().split())
s=input()
s=list(s)
if(n<=k):
    print()
else:
    str1="abcdefghijklmnopqrstuvwxyz"
    for i in range(len(str1)):
        q=s.count(str1[i])
        if(q<k):
            k-=q
            while(q):
                s.remove(str1[i])
                q-=1
        elif(q>k):
            m=k
            k-=m
            while(m):
                s.remove(str1[i])
                m-=1
            break
        else:
            while(k):
                s.remove(str1[i])
                k-=1
            break
                
    print("".join(s))
            
                
            
            
    
