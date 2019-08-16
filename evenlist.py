n=int(input("enter the number of elemnts you need  "))
a=[]
for _ in range(n):
 x=int(input())
 a.append(x) 
b = [i for i in a if i % 2 == 0]
print(" even numbers in the list")
print(b)
