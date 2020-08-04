n=int(input())
lst=[]
for i in range(n):
    lst.append(list(map(int,input().split())))
i,j=0,0
s=0
while(i!=n-1 and j!=n-1):
    if(i!=n-1 and j!=n-1):
        if(lst[i+1][j]>lst[i][j+1]):
            s+=lst[i][j+1]
            j+=1
        else:
            s+=lst[i+1][j]
            i+=1
    elif(i==n-1 and j!=n-1):
        s+=lst[i][j+1]
        j+=1
    elif(i!=n-1 and j==n-1):
        s+=lst[i+1][j]
        i+=1
print(s)
        
    
    
    
