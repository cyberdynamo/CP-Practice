n=int(input())
lst=[]
for i in range(n):
    lst.append(list(map(int,input().split())))

i=0;j=0
s=0
while(i!=n-1 and j!=n-1):
    if(lst[i][j+1]>lst[i+1][j]):
        s=(s//2)+lst[i+1][j]
        i+=1
    else:
        s=(s//2)+lst[i][j+1]
        j+=1
print(s//2+lst[n-1][n-1])
    
