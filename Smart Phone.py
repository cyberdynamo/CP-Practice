cust=int(input())
lst=[]
for c in range(cust):
    temp=int(input())
    lst.append(temp)
lst.sort()
mini=0
for i in range(cust):
    mini2=(cust-i)*lst[i]
    if(mini2>mini):
        mini=mini2
print(mini)
