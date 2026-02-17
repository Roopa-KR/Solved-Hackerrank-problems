# Given a list of integers, create a new list 
# where each element is double the value of the
# original element, except for the number 1 which should remain unchanged.
# expect output: [1, 4, 6, 8, 10]
lst=[1,2,3,4,5]
lst1=[]

for i in lst:
    if i==1:
        lst1.append(i)
    else:
        lst1.append(i*2)
print(lst1)