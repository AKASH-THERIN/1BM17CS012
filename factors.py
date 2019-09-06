import math
n=int(input("enter the number"))
a=[]

for i in range(1,math.ceil(math.sqrt(n))+1):
    if n%i==0:
        a.append(i)
        k=n/i
        if n%k==0 and k!=i:
            a.append(int(k))
a.sort()
print(a)
