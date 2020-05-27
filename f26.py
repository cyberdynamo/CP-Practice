num=int(input())
s=0
temp=num
for j in range(5,0,-1):
    s+=temp//j
    temp=temp%j
print(s)
