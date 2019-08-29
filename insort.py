
def insort1(a):
    for i in range(1,len(a)):
        temp=a[i]
        j=i-1
        while j>=0 and a[j]>temp:
             a[j+1]=a[j]
             j-=1
        a[j+1]=temp


print("enter the  elements ")
a=[int(i) for i in input().split()]
print(a)
insort1(a)
print(a)
