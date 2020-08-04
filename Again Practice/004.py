n,m=map(int,input().split())
lst=[]
for i in range(n):
    lst.append(list(map(int,input().split())))
final=[]
for i in range(n):
    for j in range(m-2):
        if(lst[i][j]==lst[i][j+1]==lst[i][j+2]):
            final.append(lst[i][j])

for i in range(n-2):
    for j in range(m):
        if(lst[i][j]==lst[i+1][j]==lst[i+2][j]):
            final.append(lst[i][j])

for i in range(n-2):
    for j in range(m-2):
        if(lst[i][j]==lst[i+1][j+1]==lst[i+2][j+2]):
            final.append(lst[i][j])

for i in range(n-2):
    for j in range(m-1,-1,-1):
        if(lst[i][j]==lst[i+1][j-1]==lst[i+2][j-2]):
            final.append(lst[i][j])

if(len(final)==0):
    print("-1")
else:
    print(min(final))

            
    
