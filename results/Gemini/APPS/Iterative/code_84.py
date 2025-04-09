def solve():
    n = int(input())
    s = input()
    sorted_s = sorted(s)

    for i in range(1 << n):
        coloring = ""
        s0 = ""
        s1 = ""
        
        for j in range(n):
            if (i >> j) & 1:
                coloring += "1"
                s1 += s[j]
            else:
                coloring += "0"
                s0 += s[j]

        s0_sorted = "".join(sorted(s0))
        s1_sorted = "".join(sorted(s1))

        merged = ""
        idx0 = 0
        idx1 = 0

        possible = True
        for j in range(n):
            if coloring[j] == '0':
                if idx0 >= len(s0_sorted):
                    possible = False
                    break
                merged += s0_sorted[idx0]
                idx0 += 1
            else:
                if idx1 >= len(s1_sorted):
                    possible = False
                    break
                merged += s1_sorted[idx1]
                idx1 += 1

        if not possible:
            continue

        if "".join(sorted_s) == merged:
            print("YES")
            print(coloring)
            return

    print("NO")

solve()