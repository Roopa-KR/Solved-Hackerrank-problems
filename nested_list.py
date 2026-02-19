#flattens a nested list and creates a new list of squares of the numbers if number is positive
data = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
res=[x**2 for row in data for x in row  if x>0]
print(res)