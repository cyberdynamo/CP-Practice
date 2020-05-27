test=int(input())
for t in range(test):
    n=int(input())
    string=input()
    set1=set(string)

    if(set1=={"Y"} or set1=={"N","Y"}):
        print("NOT INDIAN")
    elif(set1=={"I"} or set1=={"N","I"}):
        print("INDIAN")
    elif(set1=={"N"}):
        print("NOT SURE")
