def solve():
    n = int(input())
    strings = [input() for _ in range(n)]

    strings.sort(key=len)

    for i in range(1, n):
        for j in range(i):
            if strings[j] not in strings[i]:
                print("NO")
                return

    print("YES")
    for s in strings:
        print(s)

solve()