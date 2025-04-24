def solve():
    n = int(input())
    strings = []
    for _ in range(n):
        strings.append(input())

    def is_substring(a, b):
        return a in b

    strings.sort(key=len)

    for i in range(1, n):
        valid = True
        for j in range(i):
            if not is_substring(strings[j], strings[i]):
                valid = False
                break
        if not valid:
            print("NO")
            return

    print("YES")
    for s in strings:
        print(s)

solve()