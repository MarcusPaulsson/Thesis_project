def solve():
    n = int(input())
    s = input()
    sorted_s = sorted(s)

    for i in range(2**n):
        coloring = ""
        for j in range(n):
            if (i >> j) & 1:
                coloring += '1'
            else:
                coloring += '0'
        coloring = coloring[::-1]

        s0 = []
        s1 = []
        for k in range(n):
            if coloring[k] == '0':
                s0.append(s[k])
            else:
                s1.append(s[k])

        s0.sort()
        s1.sort()

        merged = []
        i = 0
        j = 0
        for k in range(n):
            if coloring[k] == '0':
                if i < len(s0):
                    merged.append(s0[i])
                    i += 1
                else:
                    break
            else:
                if j < len(s1):
                    merged.append(s1[j])
                    j += 1
                else:
                    break
        
        if "".join(merged) == "".join(sorted_s):
            print("YES")
            print(coloring)
            return

    print("NO")

solve()