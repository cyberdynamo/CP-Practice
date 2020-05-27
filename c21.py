test=int(input())
for _ in range(test):
    a,b=map(int,input().split())
    if(a>b):
        print(">")
    elif(a<b):
        print("<")
    else:
        print("=")
