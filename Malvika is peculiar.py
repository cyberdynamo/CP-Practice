test=int(input())
for t in range(test):
    string=input()
    a=string.count("a")
    b=string.count("b")
    if(a<b):
        print(a)
    else:
        print(b)
