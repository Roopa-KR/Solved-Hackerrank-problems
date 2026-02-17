# Given a list of integers, create a new list 
# where each element is even the value of list    
#expected output: [2, 4, 6, 8, 10]
lst=[1,2,3,4,5,6,7,8,9,10]
lst1=[]
for i in lst:
    if i%2==0:
        lst1.append(i)
print(lst1)
