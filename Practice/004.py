m,n=map(int,input().split())
lst=[]
for i in range(m):
    lst.append(list(map(int,input().split())))
flist=[]

for i in range(m):
    for j in range(n-2):
        if(lst[i][j]==lst[i][j+1]==lst[i][j+2]):
            flist.append(lst[i][j])
            
for i in range(m-2):
    for j in range(n):
        if(lst[i][j]==lst[i+1][j]==lst[i+2][j]):
            flist.append(lst[i][j])

for i in range(m-2):
    for j in range(n-2):
        if(lst[i][j]==lst[i+1][j+1]==lst[i+2][j+2]):
            flist.append(lst[i][j])

for i in range(m-2):
    for j in range(n-1,1,-1):
        if(lst[i][j]==lst[i+1][j-1]==lst[i-2][j-2]):
            flist.append(lst[i][j])

if(len(flist)==0):
    print(-1)
else:
    print(min(flist))
