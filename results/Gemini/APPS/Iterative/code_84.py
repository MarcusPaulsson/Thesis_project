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
        coloring_list = []

        for j in range(n):
            if coloring[j] == '0':
                s0.append(s[j])
            else:
                s1.append(s[j])
            coloring_list.append(int(coloring[j]))

        s0.sort()
        s1.sort()

        merged = []
        idx0 = 0
        idx1 = 0

        possible = True
        for k in range(n):
            if coloring[k] == '0':
                if idx0 < len(s0):
                    merged.append(s0[idx0])
                    idx0 += 1
                else:
                    possible = False
                    break
            else:
                if idx1 < len(s1):
                    merged.append(s1[idx1])
                    idx1 += 1
                else:
                    possible = False
                    break
        
        if not possible:
            continue
        
        if merged == sorted(s):
            print("YES")
            print(coloring)
            return

    print("NO")

solve()