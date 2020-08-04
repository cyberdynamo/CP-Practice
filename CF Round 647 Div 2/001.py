#Coder: cyberdynamo
for test in range(int(input())):
    a,b=map(int,input().split())
    if(a<b):
        if(b%2!=0 and b%4!=0 and b%8!=0):
            print("-1")
        else:
            if(b%a!=0):
                print("-1")
            else:
                b=b//a
                c1,c2,c3=0,0,0
                g=0
                c1=b%8
                if(c1==0):
                    temp=b//8
                    g+=temp
                    b=b//(temp*8)
                c2=b%4
                if(c2==0):
                    temp=b//4
                    g+=temp
                    b=b//(temp*4)
                c3=b%2
                if(c3==0):
                    temp=b//2
                    g+=temp
                    b=b//(temp*2)
                print(g)
    elif(a==b):
        print(0)
    
        
