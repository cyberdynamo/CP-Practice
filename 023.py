import itertools
l=int(input())
lst=[]
for i in range(l):
    lst.append(list(input().split()))

newlist=list(itertools.permutations(lst,l))
print(newlist)
string=""
for i in range(l):
    tmpstring="".join(newlist[i])
print(string)
        
