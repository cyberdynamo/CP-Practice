import itertools

list1=[]

s=str(input())

res = [s[i: j] for i in range(len(s)) 

          for j in range(i + 1, len(s) + 1)]

def pronic(s1):

    set1=[]

    set2=[]

    for p in range(0,len(s1)-1):

        a=int(s1[p])
    
        b=int(s1[p+1])

        mul=int(a*b)

        mul=str(mul)

        if mul in res:

            set1.append(mul)

    if (len(set1)==0):

        print("-1")

    else:    

        print(set1)

pronic((s))
