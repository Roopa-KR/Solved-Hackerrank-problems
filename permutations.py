from itertools import permutations

# Take input in one line
s, k = input().split()

# Convert k to integer
k = int(k)

# Generate permutations (sorted as per Hackerrank style)
for p in permutations(sorted(s.upper()), k):
    print("".join(p))