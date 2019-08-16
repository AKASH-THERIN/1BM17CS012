def fib(n):
    a=0
    b=1
    if n<0:
        print("enter n>1")
    elif n==1:
        print(0)
    elif n==2:
        print(1)
    else:
        for i in range(n):
            print(a)
            c=a+b
            a=b
            b=c

n=int(input("enter numbers in series  "))
fib(n)
        
           
