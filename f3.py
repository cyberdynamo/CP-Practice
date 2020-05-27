test=int(input())
for _ in range(test):
    string=input()
    l=len(string)
    if(l>10):
        print("{}{}{}".format(string[0],l-2,string[-1]))
    else:
        print(string)
