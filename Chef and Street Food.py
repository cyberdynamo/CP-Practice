test=int(input())
for t in range(test):
    n=int(input())
    maxi=0
    score=0
    for i in range(n):
        S,P,V=map(int,input().split())
        temp=P//(S+1)
        score=temp*V
        if(score>maxi):
            maxi=score
    print(maxi)
