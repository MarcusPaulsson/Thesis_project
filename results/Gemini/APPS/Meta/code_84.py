def solve():
    n = int(input())
    s = input()

    for i in range(1 << n):
        coloring = ""
        for j in range(n):
            if (i >> j) & 1:
                coloring += "1"
            else:
                coloring += "0"

        s0 = ""
        s1 = ""
        for j in range(n):
            if coloring[j] == '0':
                s0 += s[j]
            else:
                s1 += s[j]

        sorted_s0 = "".join(sorted(list(s0)))
        sorted_s1 = "".join(sorted(list(s1)))

        merged = ""
        idx0 = 0
        idx1 = 0
        
        temp_merged = []
        
        for k in range(n):
            if coloring[k] == '0':
                if idx0 < len(sorted_s0):
                    temp_merged.append(sorted_s0[idx0])
                    idx0 += 1
                else:
                    temp_merged.append('z' + chr(ord('z') + 1))
            else:
                if idx1 < len(sorted_s1):
                    temp_merged.append(sorted_s1[idx1])
                    idx1 += 1
                else:
                    temp_merged.append('z' + chr(ord('z') + 1))
        
        
        is_sorted = True
        for k in range(n - 1):
            if temp_merged[k] > temp_merged[k+1]:
                is_sorted = False
                break

        if is_sorted:
            print("YES")
            print(coloring)
            return

    print("NO")

solve()