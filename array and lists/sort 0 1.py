from sys import stdin

def sortZeroesAndOne(arr, n) :
    #Your code goes here 
    # zeroes = 0
    # ones = 0
    # for i in arr:
    #     if i == 0:
    #         zeroes = zeroes + 1
    #     if i == 1:
    #         ones = ones + 1
    # for j in range(zeroes):
    #     arr[j] = 0
    
    # for k in range(1, ones+1):
    #     arr[-k] = 1

    s = 0
    for i in range(n):
        if arr[i] == 0:
            j = arr[s]
            arr[s] = arr[i]
            arr[i] = j
            s += 1





















#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().strip())

    if n == 0 :
        return list(), 0

    
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n) :
    for i in range(n) :
        print(arr[i], end = ' ')
    


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    sortZeroesAndOne(arr, n)
    printList(arr, n)
    print()

    t -= 1
