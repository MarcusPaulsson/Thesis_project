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
        
        s0 = "".join(sorted(s0))
        s1 = "".join(sorted(s1))
        
        merged = ""
        idx0 = 0
        idx1 = 0
        
        coloring_check = ""
        
        for j in range(n):
            if coloring[j] == '0':
                merged += s0[idx0]
                coloring_check += '0'
                idx0 += 1
            else:
                merged += s1[idx1]
                coloring_check += '1'
                idx1 += 1
        
        if "".join(sorted(s)) == merged:
            print("YES")
            print(coloring)
            return
    
    print("NO")

solve()