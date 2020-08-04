n=int(input())
for i in range(n):
    lst=list(map(int,input().split()))
    if(sum(lst)==0):
        print("Beginner")
    elif(sum(lst)==1):
        print("Junior Developer")
    elif(sum(lst)==2):
        print("Middle Developer")
    elif(sum(lst)==3):
        print("Senior Developer")
    elif(sum(lst)==4):
        print("Hacker")
    else:
        print("Jeff Dean")
