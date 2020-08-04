for t in range(int(input())):
    n=int(input())
    s=input()
    count=0
    var=0
    for i in range(len(s)):
        if(s[i]=="("):
            var+=1
        else:
            var-=1
        if(var<0):
            count+=1
            var=0
    print(count)
