
# N=int(input())
# for i in range(N):
#    # print(1,end="")
#     for j in range(1, (N+1) - i): 
#         print(j,end="")
#     print()
n=int(input())
for i in range(1,n+1):
    print("1",end="")
    for j in range(1,(n-i)+1):
        print(j+1,end="")
    print()
