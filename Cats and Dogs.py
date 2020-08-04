test=int(input())
for t in range(test):
    c,d,l=map(int,input().split())

    if(c==0):
        if(d*4==l):
            print("yes")
        else:
            print("no")
    elif(d==0):
        if(c*4==l):
            print("yes")
        else:
            print("no")
    else:
        mini=d*4
        if(c>d*2):
            mini+=(4*(c-d*2))
        maxi=d*4+c*4

        if(l>=mini and l<=maxi and l%4==0):
            print("yes")
        else:
            print("no")
