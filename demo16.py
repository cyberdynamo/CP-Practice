'''arr=[1,2,3,4,5,6,7,8,9]
m1,m2,m3=-1,-1,-1
for i in range(len(arr)):
    if(arr[i]>m1):
        m3=m2
        m2=m1
        m1=arr[i]
    elif(arr[i]>m2):
        m3=m2
        m2=arr[i]
    elif(arr[i]>m1):
        m3=arr[i]
print(m1,m2,m3)'''
print('-inf')
if(float('-inf')<2):
    print("YES")
