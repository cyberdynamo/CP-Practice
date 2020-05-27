import decimal
def dropzeros(number):
    mynum = decimal.Decimal(number).normalize()
    return mynum.__trunc__() if not mynum % 1 else float(mynum)
number=int(input())
lst=[]
def median(l):
    length=len(l)
    tmplst=l.copy()
    tmplst.sort()
    if(length==1):
        return tmplst[0]
    else:
        if(length%2==1):
            mid=length//2
            return tmplst[mid]
        else:
            mid1=length//2
            mid2=mid1-1
            var=(tmplst[mid1]+tmplst[mid2])/2
            return dropzeros(var)
for i in range(number):
    op,num=input().split()
    num=int(num)
    if(op=="r"):
        if(num not in lst):
            print("Wrong!")
        else:
            lst.remove(num)
            if(len(lst)==0):
                print("Wrong!")
            else:     
                print(median(lst))
    elif(op=="a"):
        lst.append(num)
        print(median(lst))
        
