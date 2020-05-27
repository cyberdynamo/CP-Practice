test=int(input())
for t in range(test):
    string=input()
    a=string.count("0")
    b=string.count("1")
    if(a==1 or b==1):
        print("YES")
    else:
        print("NO")
