string="xyz"
for t in range(int(input())):
    n =int(input())
    if(n==3):
        print(string)
    elif(n<3):
        print(string[0:n])
    else:
        string2=string*(n//3)+string[0:n%3]
        print(string2)
