def merge_the_tools(string, k):
    partition_size=(len(string))//k
    l=''
    for i in range(0,len(string),partition_size):
        l=string[i:i+partition_size]
        res=''
        for ch in l:
            if ch not in res:
                res=res+ch
        print(res)
        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)