def solve():
    n = int(input())
    strings = []
    for _ in range(n):
        strings.append(input())

    strings.sort(key=len)

    for i in range(1, n):
        found = False
        for j in range(i):
            if strings[j] in strings[i]:
                found = True
                break
        if not found:
            print("NO")
            return

    print("YES")
    for s in strings:
        print(s)

solve()