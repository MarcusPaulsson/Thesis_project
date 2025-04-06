def solve():
    n = int(input())
    s = input()

    for i in range(2**n):
        coloring = ""
        for j in range(n):
            if (i >> j) & 1:
                coloring += "1"
            else:
                coloring += "0"
        
        color0 = ""
        color1 = ""
        for j in range(n):
            if coloring[j] == '0':
                color0 += s[j]
            else:
                color1 += s[j]
        
        sorted_color0 = "".join(sorted(color0))
        sorted_color1 = "".join(sorted(color1))
        
        merged = ""
        idx0 = 0
        idx1 = 0
        
        coloring_check = ""
        
        
        for k in range(n):
            
            
            if idx0 < len(sorted_color0) and (idx1 == len(sorted_color1) or sorted_color0[idx0] <= sorted_color1[idx1]):
                merged += sorted_color0[idx0]
                idx0 += 1
                coloring_check += '0'
                
            else:
                merged += sorted_color1[idx1]
                idx1 += 1
                coloring_check += '1'
        
        
        if "".join(sorted(s)) == merged:
            print("YES")
            print(coloring)
            return
    
    print("NO")

solve()