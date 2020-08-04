n=int(input())
a=list(input())
b=list(input())
for i in a:
    if(i in b):
        b.remove(i)
    else:
        break
print(len(b),end="")
