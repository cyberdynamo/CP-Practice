#Coder: cyberdynamo
for t in range(int(input())):
    k=int(input())
    k-=1
    for i in range(k):
        print(".",end="")
    print("O",end="")
    for i in range(8-k-1):
        print("X",end="")
    print()

    if(k!=7):
        for i in range(k+2):
            print("X",end="")
    if(k==7):
        for j in range(8):
            print("X",end="")
    for i in range(8-(k+2)):
        print(".",end="")
    print()


    for j in range(6):
        for k in range(8):
            print(".",end="")
        print()
