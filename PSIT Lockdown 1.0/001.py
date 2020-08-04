t =int(input())
s="abc"
if t in range(1,101):
    for i in range(1,t+1):
        n =int(input())
        if(n< 3):
            print(s[0:n])
        elif(n==3):
            print(s)
        else:
            quo=n/3
            r=n%3
            news=s*quo+s[0:r]
            print(news)
