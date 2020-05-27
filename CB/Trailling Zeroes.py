num=int(input())
count=0
i=1
while(num//(5**i)!=0):
    count+=num//(5**i)
    i+=1
print(count)
