n=int(input())
lst=list(map(int,input().split()))
dict1={}

for i in range(len(lst)):
    if(lst[i] not in dict1):
        dict1.update({lst[i]:1})
    else:
        temp=dict1[lst[i]]
        dict1.update({lst[i]:temp+1})
print(max(dict1.values()))
