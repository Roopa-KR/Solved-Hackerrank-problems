#Fibonacci series:
a=0
b=1
n=int(input())
for i in range(1,n):
    print(a)
    c=a+b
    a=b
    b=c