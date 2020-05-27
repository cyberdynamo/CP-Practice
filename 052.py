import itertools
string=input()
lst=list(string)
lst2=list(itertools.permutations(lst))
for i in lst2:
    for j in i:
        print(j,end="")
    print(end=" ")
