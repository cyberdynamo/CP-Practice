import collections
def fun1(n,lst):
    m=collections.Counter(lst).most_common()
    while(n>=m[-1][1]):
        n-=m.pop()[1]
    return len(m)

n=int(input())
lst=list(map(int,input().split()))
print(fun1(n,lst))
