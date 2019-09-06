import random
st=""
for i in range(34,127):
    st=st+chr(i)
le=int(input("enter the leng"))
p="".join(random.sample(st,le))
print(p)
