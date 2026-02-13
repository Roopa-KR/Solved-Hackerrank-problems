def check_time(string, subs):
    count = 0
    for j in range(len(string) - len(subs) + 1):
        if string[j:j+len(subs)] == subs:
            count += 1
    return count

if __name__ == "__main__":
    string = input()
    subs = input()
    print(check_time(string, subs))
