a=int(input())
b=int(input())
c=int(input())
c1,c2,c3,c4,c5,c6=a*b+c,a+b*c,a*b*c,a+b+c,a*(b+c),(a+b)*c
print(max(c1,c2,c3,c4,c5,c6))
