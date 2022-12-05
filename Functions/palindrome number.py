num=int(input())
p=num
r=0

while p!=0:
    r =(r*10)+p%10
    p=p//10
if (num==r):
    print("true")
else:
    print("false")
