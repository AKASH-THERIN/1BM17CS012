st=""
li1=open("file1.txt",'r').read().split()#welcome to bmsce
li2=open("file2.txt",'r').read().split() #what is your name
print(" ".join(li1))
print(" ".join(li2))
for i in range(max(len(li1),len(li2))):
    if i <len(li1):
        st+=(li1[i][:len(li1[i])/2])
    if i<len(li2):
        st+=(li2[i][:len(li2[i])/2])
    st+=" "
file3=open("file3.txt",'w')
file3.write(st)
file3.close()
print(open("file3.txt",'r').read())
