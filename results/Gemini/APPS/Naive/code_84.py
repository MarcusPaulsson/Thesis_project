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
        
        zeros = ""
        ones = ""
        for j in range(n):
            if coloring[j] == '0':
                zeros += s[j]
            else:
                ones += s[j]
        
        sorted_zeros = "".join(sorted(zeros))
        sorted_ones = "".join(sorted(ones))
        
        merged = ""
        zero_idx = 0
        one_idx = 0
        
        for j in range(n):
            if coloring[j] == '0':
                merged += sorted_zeros[zero_idx]
                zero_idx += 1
            else:
                merged += sorted_ones[one_idx]
                one_idx += 1
        
        if merged == "".join(sorted(s)):
            print("YES")
            print(coloring)
            return
    
    print("NO")

solve()