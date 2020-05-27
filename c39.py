    test=int(input())
    for t in range(test):
        a,b,c=map(float,input().split())

        if(a>50 and b<0.7 and c>5600):
            grade=10
        elif(a>50 and b<0.7 and c<=5600):
            grade=9
        elif(a<=50 and b<0.7 and c>5600):
            grade=8
        elif(a>50 and b>=0.7 and c>5600):
            grade=7
        elif(a>50 and b>=0.7 and c<=5600):
            grade=6
        elif(a<=50 and b<0.7 and c<=5600):
            grade=6
        elif(a<=50 and b>=0.7 and c>5600):
            grade=6
        elif(a<=50 and b>=0.7 and c<=5600):
            grade=5
        print(grade)
        
