lst=list(map(int,input().split("+")))
lst.sort()
for i in range(len(lst)-1):
    print(lst[i],end="+")
print(lst[-1])
