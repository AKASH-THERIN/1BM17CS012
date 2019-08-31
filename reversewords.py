li=[x for x in input("enter the string").split()]
print(li[::-1 ])
for i in reversed(range(len(li))):
    print(li[i][::-1],end= " ")
