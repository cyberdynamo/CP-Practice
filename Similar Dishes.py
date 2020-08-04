for t in range(int(input())):
    a=input().split()
    b=input().split()

    a=set(a)
    b=set(b)

    if(len(a.union(b))<=6):
        print("similar")
    else:
        print("dissimilar")
