#Amstrong number
n=int(input())#Example give 153 as input
temp=n
digit=0
while n!=0:
    rem=n%10
    digit=digit+rem**3  # digit = 1**3 + 5**3 + 3**3
    n=n//10
if  digit==temp :
    print("its a amstrong number")
else:
    print( "Its not an amstrong number")