def solve():
    s = input()
    n = len(s)
    t = []
    u = ""

    suffix_min = [""] * (n + 1)
    suffix_min[n] = chr(ord('z') + 1)

    for i in range(n - 1, -1, -1):
        suffix_min[i] = min(s[i], suffix_min[i + 1])

    i = 0
    while i < n or len(t) > 0:
        if len(t) > 0 and t[-1] <= suffix_min[i if i < n else n]:
            u += t[-1]
            t.pop()
        else:
            if i < n:
                t.append(s[i])
                i += 1
            else:
                break

    while len(t) > 0:
        u += t[-1]
        t.pop()

    print(u)


solve()