n=int(input())
odd=0
even=0
x=0
while n>0:
    x=n%10
    if x%2==0:
        even=even+x
    else:
        odd=odd+x
    n=n//10    
print((even),(odd))
