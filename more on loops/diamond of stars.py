n=int(input())
for i in range((n+1)//2):
    print(" "*(((n+1)//2)-(i+1)),end="")
    print("*"*(2*i+1),end="")
    print()
    
for k in range(1, ((n-1)//2)+1):
    print(" "*k, end="")
    print("*"*(n-2*k), end="")
    print()
