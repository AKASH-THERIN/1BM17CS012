def heap_check(ar):
    for i in range(int(len(ar)/2)-1):
        if ar[i]>=max(ar[2*i],ar[2*i+1]):
            continue
        return False
    return True

#driver
ar=[int(i) for i in input("enter the heap").split()]
print(ar)
print(heap_check(ar))
