#cartesian product of two lists with a condition
# Using list comprehension to create a list of
# # pairs (x, y) where x is from the list [1, 2, 3] and y is from the list [3, 4, 5],
# but only include pairs where the sum of x and y is even.
pairs = [
    (x, y)
    for x in [1,2,3]
    for y in [3,4,5]
    if (x + y) % 2 == 0
]
