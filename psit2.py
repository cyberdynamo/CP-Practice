test=int(input())
def median(tmplst):
    tmplst.sort()
    n=len(tmplst)
    if(n%2!=0):
        return tmplst[n//2]
    else:
        return ((tmplst[n//2]+tmplst[n//2-1])/2)
lst=[]
for t in range(test):
    lst.append(int(input()))
    print("{:0.1f}".format(median(lst)))
