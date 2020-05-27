def findgcd(x, y):
   while(y):
      x, y = y, x % y
   return x

test=int(input())
for _ in range(test):
    n,*l=map(int,input().split())
    num1=l[0]
    num2=l[1]
    gcd=findgcd(num1,num2)
    for i in range(2,len(l)):
       gcd=findgcd(gcd,l[i])

    for i in l:
        print(i//gcd,end=" ")
    print("\n")
