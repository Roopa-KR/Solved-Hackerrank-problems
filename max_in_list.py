lst=[9,2,1,6,33,90,1]
len(lst)
maxi=0
for i in range(len(lst)):
    if lst[i]>maxi:
        maxi=lst[i]
print(maxi)