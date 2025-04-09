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

        sorted_s = sorted(s)
        
        merged_s = ""
        idx0 = 0
        idx1 = 0
        
        possible = True
        merged_s = ""
        
        idx0 = 0
        idx1 = 0
        
        for char in sorted_s:
            if idx0 < len(s0) and s0[idx0] == char:
                merged_s += '0'
                idx0 += 1
            elif idx1 < len(s1) and s1[idx1] == char:
                merged_s += '1'
                idx1 += 1
            else:
                possible = False
                break

        if possible:
            
            coloring_result = ""
            
            idx0 = 0
            idx1 = 0
            
            result_coloring = ""
            
            for k in range(n):
                if coloring[k] == '0':
                    
                    if idx0 < len(s0) and s[k] == s0[idx0]:
                        result_coloring += '0'
                        idx0 += 1
                    else:
                        result_coloring = None
                        break
                else:
                    if idx1 < len(s1) and s[k] == s1[idx1]:
                        result_coloring += '1'
                        idx1 += 1
                    else:
                        result_coloring = None
                        break
                        
            if result_coloring != None:
                print("YES")
                print(coloring)
                return

    print("NO")

solve()