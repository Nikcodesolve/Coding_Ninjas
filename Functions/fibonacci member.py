
def fib(n):
    if n==0 or n==1 or n==2:
       return True
    f1=0
    f2=1
    for i in range(n):
        f3=f1+f2
        f1=f2
        f2=f3
        if n==f2:
            return True
        return False
        

n=int(input())
if fib(n):
    print("true")
else:
        print("false")
