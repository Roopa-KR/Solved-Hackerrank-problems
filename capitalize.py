def solve(s):
    result = []
    capitalize_next = True

    for ch in s:
        if ch == ' ':
            capitalize_next = True
            result.append(ch)
        else:
            if capitalize_next:
                result.append(ch.upper())
                capitalize_next = False
            else:
                result.append(ch)
    return ''.join(result)
s=input()
print(solve(s))