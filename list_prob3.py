# Given a list of integers, create a new list
#expected output: [1, 20, 11, 9]
l=[1,20,11,4,78,9,0,20] #impppppppppppppp create new list from the existing
ex = [78,0,4]
res = []
for i in l:
    if i not in ex and i not in res:
        res.append(i)
print(res)