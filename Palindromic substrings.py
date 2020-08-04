for t in range(int(input())):
    a=set(list(input()))
    b=set(list(input()))

    if(len(a.union(b))<len(a)+len(b)):
        print("YES")
    else:
        print("NO")
