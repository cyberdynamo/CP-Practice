n=1
while(n!=0):
    n=int(input())
    lst=list(map(int,input().split()))
    lst2=[0]*len(lst)
    for i in range(len(lst)):
        lst2[lst[i]]=i
    print(lst,lst2)
    if(lst==lst2):
        print("ambiguous")
    else:
        print("not ambiguous")
