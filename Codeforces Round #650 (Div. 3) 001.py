for t in range(int(input())):
    n,k=map(int,input().split())
    s=input()
    s=list(s)
    l=len(s)
    i,j=0,0
    while(i<n):
        if(s[i]=="1"):
            i+=1
            j=0
            while(j<k):
                if(i>=l):
                    break
                s[i]="a"
                i+=1
                j+=1
            i-=1
        i+=1
    i=l-1
    while(i>=0):
        if(s[i]=="1"):
            i-=1
            j=0
            while(j<k):
                if(i<0):
                    break
                s[i]="a"
                i-=1
                j+=1
            i+=1
        i-=1


    c=0
    flag=0
    i=0
    while(i<l):
        if(s[i]=="0"):
            s[i]="b"
            c+=1
            i=i+k+1

            if(i>=l):
                break
            i-=1
        i+=1
    print(c+flag)
            
                
            
                
                
    
