wamt,iamt=input().split()
wamt=int(wamt)
iamt=float(iamt)
format(iamt,".2f")
print(iamt)

if(wamt%5==0):
    if((wamt+0.5)<=iamt):
        print("{0:.2f}".format(iamt-(wamt+0.5)))
    else:
        print(iamt)
else:
    print(iamt)
