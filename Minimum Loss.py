n=int(input())
lst1=list(map(int,input().split()))
lst2=[]
for i in range(n):
    tmplst=[lst1[i], i]
    lst2.append(tmplst)
mini=99999999999999999
lst2.sort()
for i in range(n-1):
    if((lst2[i+1][0]-lst2[i][0])<mini and (lst2[i][1]>lst2[i+1][1])):
        mini=lst2[i+1][0]-lst2[i][0]
print(mini)
