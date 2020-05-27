test=int(input())
for _ in range(test):
    str1=input()
    if(str1=="B" or str1=="b"):
        print("BattleShip")
    elif(str1=="C" or str1=="c"):
        print("Cruiser")
    elif(str1=="D" or str1=="d"):
        print("Destroyer")
    else:
        print("Frigate")
    
