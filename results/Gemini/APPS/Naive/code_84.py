def solve():
    n = int(input())
    s = input()

    for i in range(1 << n):
        coloring = ""
        for j in range(n):
            if (i >> j) & 1:
                coloring += '1'
            else:
                coloring += '0'

        zeros = ""
        ones = ""
        for j in range(n):
            if coloring[j] == '0':
                zeros += s[j]
            else:
                ones += s[j]

        sorted_s = "".join(sorted(s))
        
        merged = ""
        zero_idx = 0
        one_idx = 0
        
        possible = True
        for char in sorted_s:
            if zero_idx < len(zeros) and zeros[zero_idx] == char:
                merged += zeros[zero_idx]
                zero_idx += 1
            elif one_idx < len(ones) and ones[one_idx] == char:
                merged += ones[one_idx]
                one_idx += 1
            else:
                possible = False
                break
        
        if possible:
            print("YES")
            print(coloring)
            return
    
    print("NO")

solve()