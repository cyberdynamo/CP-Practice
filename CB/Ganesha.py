n=int(input())
v="*"

print(v,end="")
for i in range(n//2-1):
    print(" ",end="")
for i in range(n//2):
    print(v,end="")
print(v)


#step 2
for i in range(n//2-1):
    print(v,end="")
    for j in range(n//2-1):
        print(" ",end="")
    print(v)

#step 3
for i in range(n-1):
    print(v,end="")
print(v)


#Step 4
for i in range(n//2-1):
    for j in range(n//2):
        print(" ",end="")
    print(v,end="")
    for k in range(n//2-1):
        print(" ",end="")
    print(v)
#Step 5
for i in range(n//2+1):
    print(v,end="")
for i in range(n//2-1):
    print(" ",end="")
print(v)
