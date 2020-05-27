test=int(input())
for t in range(test):
      n=int(input())
      lst=list(map(int,input().split()))
##    i=0
##    s=0
##    while(i<n-1):
##        if(lst[i]<lst[i+1]):
##            s+=lst[i]
##            lst.pop(i+1)
##            n-=1
##        else:
##            s+=lst[i+1]
##            lst.pop(i)
##            n-=1
##    print(s)
      lst.sort()
      print(lst[0]*(n-1))
