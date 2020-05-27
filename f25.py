string=input()
c=0
for i in string:
    if(i=="H" or i=="Q" or i=="9"):
        print("YES")
        c=1
        break
if(c==0):
    print("NO")
