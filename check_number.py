def chekker(s):
    print(any(c.isalnum() for c in s))   # 1. any alphanumeric
    print(any(c.isalpha() for c in s))   # 2. any alphabetical
    print(any(c.isdigit() for c in s))   # 3. any digit
    print(any(c.islower() for c in s))   # 4. any lowercase
    print(any(c.isupper() for c in s))   # 5. any uppercase

if __name__ == "__main__":
    s = input()
    chekker(s) any alphanumeric
    print(any(c.isalpha() for c in s))   # 2. any alphabetical ,any digit,any lowercase, any uppercase