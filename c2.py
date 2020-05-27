wamt,iamt=input().split()
wamt=int(wamt)
iamt=float(iamt)

if(wamt%5==0):
    if(iamt-(wamt+0.5)>=0):
        print("{:.2f}".format(iamt-(wamt+0.5)))
    else:
        print("{:0.2f}".format(iamt))
else:
    print("{:0.2f}".format(iamt))
