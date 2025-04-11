def solve():
    n = int(input())
    s = input()

    def check(coloring):
        s0 = ""
        s1 = ""
        for i in range(n):
            if coloring[i] == '0':
                s0 += s[i]
            else:
                s1 += s[i]
        
        s0_sorted = "".join(sorted(s0))
        s1_sorted = "".join(sorted(s1))
        
        sorted_s = "".join(sorted(s))
        
        merged = ""
        i = 0
        j = 0
        k = 0
        
        while i < len(s0_sorted) or j < len(s1_sorted):
            if i < len(s0_sorted) and (j == len(s1_sorted) or s0_sorted[i] <= s1_sorted[j]):
                merged += s0_sorted[i]
                i += 1
            else:
                merged += s1_sorted[j]
                j += 1
        
        return merged == sorted_s

    for i in range(2**n):
        coloring = bin(i)[2:].zfill(n)
        if check(coloring):
            print("YES")
            print(coloring)
            return
    
    print("NO")

solve()