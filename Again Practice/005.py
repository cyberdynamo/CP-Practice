import collections
n=int(input())
lst=list(map(int,input().split(",")))

def fun1(n,lst):
    common=collections.Counter(lst).most_common()
    while(n>=common[-1][1]):
        n-=common.pop()[1]
    return len(common)
print(fun1(n,lst))
