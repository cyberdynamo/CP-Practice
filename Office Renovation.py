w=4
h=3
boundaryType=[1,1]
boundaryDist=[1,3]
area=w*h
n=len(boundaryType)
for i in range(n):
    if(boundaryType[i]==0):
        h-=boundaryDist[i]
        print(w*h)
    else:
        w-=boundaryDist[i]
        print(w*h)
    

