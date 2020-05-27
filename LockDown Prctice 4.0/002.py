def gcd (a,b):
    if (b == 0):
        return a
    else:
         return gcd (b, a % b)

n,k=map(int,input().split())
lst=list(map(int,input().split()))
tmplst=[]
tmplst.append(lst[0]-k)
for i in range(1,len(lst)):
    tmplst.append(lst[i]-lst[i-1])

res = tmplst[0]
for c in tmplst[1::]:
    res = gcd(res , c)
print(abs(res))
