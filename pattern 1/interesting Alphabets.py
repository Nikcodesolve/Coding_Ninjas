
n=int(input())
i=1
while i<=n:
    j=1
    while j<=i:
        print(chr(65+n-i+j-1),end="")
        j+=1
    print()    
    i+=1
