n=int(input())
lst=list(map(int,input().split()))
lst2=[]
for i in range(n):
    lst2.append([lst[i],i])
lst2.sort(reverse=True)
print(lst2)
mini=999999999999
for i in range(1,len(lst2)):
    if((lst2[i-1][1]<lst2[i][1]) and (lst2[i-1][0]-lst2[i][0]<mini)):
        mini=lst2[i-1][0]-lst2[i][0]
print(mini)
