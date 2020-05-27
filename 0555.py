n=int(input())
lst=list(map(int,input().split()))
def fun(lst):
    print(len(lst))
    for i in range(1,len(lst)):
        if(lst[i-1]>lst[i]):
            lst.remove(lst[i-1])
            fun(lst)
            print(lst)
fun(lst)
print(len(lst))

    
