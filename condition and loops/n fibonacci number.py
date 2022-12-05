
n = int(input())
f1 = 1
f2 = 1
f3=0
if n==1 or n==2:
  print(1)
else:
  n-=2
  while(n>0):
    f3 = f1+f2    
    f1 = f2
    f2 = f3
    n-=1
  print(f3)
