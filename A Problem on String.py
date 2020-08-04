n=int(input())
s=input()
q=int(input())
for i in range(q):
    a,b=input().split()
    x=s.count(a)
    y=s.count(b)

    if(a==b):
        print(x*(x-1)//2)
    else:
        print(x*y)
