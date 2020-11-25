#Suraj Pawar
def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        ip = string[i:i+k]
        ip = list(dict.fromkeys(ip))
        for j in range(0,len(ip)):
            print(ip[j], end='')
        print()

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)