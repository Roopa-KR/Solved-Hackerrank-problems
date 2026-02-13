def mutate_string(string, position, character):
    strg=string
    l=list(strg)
    l[position]=character
    strg=''.join(l)
    
    return strg

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)