def solve(words):
    for w in words:
        if w and w[0].isalpha():
            result.append(w[0].upper()+w[1:])
        else:
            print(w)
    print(' '.join(result))
s=input()
words=s.split()
result=[]
solve(words)