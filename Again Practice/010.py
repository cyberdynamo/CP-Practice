string=input()
l=len(string)

for loc in range(l//2,0,-1):
    prefix=string[:loc]
    suffix=string[l-loc:]
    if(prefix==suffix):
        print(loc)
        break
    elif((prefix!=suffix) and loc==1):
        print("-1")
