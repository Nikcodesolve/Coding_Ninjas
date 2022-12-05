
N=int(input())
rev = 0
x=N
while(N > 0):
    rev = rev * 10 + N % 10
    N = N // 10
#  print(rev))
if(x==rev):
    print("true")
else:
    print("false")
    
