n=int(input())
lst=[0]*n
for i in range(n):
    lst[i]=int(input())

lst.sort()
print(*lst)
