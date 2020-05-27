for t in range(int(input())):
    n=int(input())
    l=list(map(int,input().split(' ')))
    if l==l[::-1] and set(l)=={1,2,3,4,5,6,7}:
        print('yes')
    else:
        print('no')
