
## Read input as specified in the question
## Print the required output in given format
N=int(input())
i=1
while i<=N:
    j=1
    while j<=i:
        print(chr(65+i+j-2),end="")
        j+=1
    print()
    i+=1 
