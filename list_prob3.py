# Given a list of integers, create a new list
#expected output: [1, 20, 11, 4, 9]
l=[1,20,11,4,78,9,0,20]
lst=[]
for i in l[:4]:
    lst.append(i)
lst.append(l[5])
print(lst)