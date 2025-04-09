def solve():
    n = int(input())
    s = input()

    def check(coloring):
        zeros = []
        ones = []
        for i in range(n):
            if coloring[i] == '0':
                zeros.append(s[i])
            else:
                ones.append(s[i])
        
        zeros.sort()
        ones.sort()
        
        merged = []
        zero_idx = 0
        one_idx = 0
        for i in range(n):
            if coloring[i] == '0':
                merged.append(zeros[zero_idx])
                zero_idx += 1
            else:
                merged.append(ones[one_idx])
                one_idx += 1
                
        
        sorted_s = sorted(s)
        
        if merged == sorted_s:
            return True
        else:
            return False
        
    for i in range(2**n):
        coloring = bin(i)[2:].zfill(n)
        if check(coloring):
            print("YES")
            print(coloring)
            return
    
    print("NO")

solve()