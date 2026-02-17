from itertools import combinations

s, k = input().split()
k = int(k)

for i in range(1, k + 1):
    for p in combinations(sorted(s.upper()), i):
        print("".join(p))