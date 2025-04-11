def solve():
    n = int(input())
    s = input()
    sorted_s = sorted(s)

    for i in range(1 << n):
        coloring = ""
        for j in range(n):
            if (i >> j) & 1:
                coloring += "1"
            else:
                coloring += "0"

        s0 = []
        s1 = []
        for j in range(n):
            if coloring[j] == '0':
                s0.append(s[j])
            else:
                s1.append(s[j])

        s0.sort()
        s1.sort()

        merged = []
        idx0 = 0
        idx1 = 0
        for j in range(n):
            if coloring[j] == '0':
                merged.append(s0[idx0])
                idx0 += 1
            else:
                merged.append(s1[idx1])
                idx1 += 1

        if merged == sorted_s:
            print("YES")
            print(coloring)
            return

    print("NO")

solve()