n=int(input())
s=input()
tmp=[]
for i in range(0,n):
    j=0
    for j in range(i-1,i//2-1,-1):
        if(s[j]==s[i]):
            break
    print(j)
    if(j!=i//2):
        tmp.append(tmp[j]+1)
    else:
        tmp.append(s[:i].count(s[i]))

q=int(input())
for t in range(q):
    m=int(input())
    print(tmp[m-1])
