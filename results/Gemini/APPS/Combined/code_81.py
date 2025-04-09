def solve():
    n = int(input())
    strings = []
    for _ in range(n):
        strings.append(input())

    strings.sort(key=len)

    def is_substring(a, b):
        return a in b

    possible = True
    for i in range(1, n):
        if not is_substring(strings[i-1], strings[i]):
            possible = False
            break

    if possible:
        print("YES")
        for s in strings:
            print(s)
    else:
        print("NO")

solve()