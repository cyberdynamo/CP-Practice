lst=[]
for t in range(int(input())):
    x,y,a,b,c,d=map(int,input().split())

    f=a*50+b*5+c*10+d*20
    z=f-y
    lst.append([z,x,y+z])
lst.sort(reverse=True)
for i in range(5):
    print(lst[i][1],lst[i][2])
