n=int(input())
lst=list(map(int,input().split()))
maximum=0
for i in range(n-1):
    for j in range(i+1,n):
        tmplst=lst[i:j+1]
        mini=min(tmplst)
        maxi=max(tmplst)
        tmp= (((mini & maxi) ^ (mini| maxi)) & (mini ^ maxi))
        maximum=max(tmp,maximum)
print(maximum)
