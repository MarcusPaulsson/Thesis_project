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
        
        s0_sorted = "".join(sorted(s0))
        s1_sorted = "".join(sorted(s1))
        
        merged = ""
        i0 = 0
        i1 = 0
        
        coloring_check = ""

        for j in range(n):
          if coloring[j] == '0':
            if i0 < len(s0_sorted):
              merged += s0_sorted[i0]
              i0 += 1
              coloring_check += '0'
            else:
              break
          else:
            if i1 < len(s1_sorted):
              merged += s1_sorted[i1]
              i1 += 1
              coloring_check += '1'
            else:
              break

        if len(merged) == n and "".join(sorted(s)) == merged:
            print("YES")
            print(coloring)
            return
    
    print("NO")

solve()