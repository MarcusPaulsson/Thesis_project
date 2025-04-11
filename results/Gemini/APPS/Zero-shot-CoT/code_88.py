def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    counts = {}
    for x in a:
        counts[x] = counts.get(x, 0) + 1
    
    matrix = [[0] * n for _ in range(n)]
    
    def can_place(r, c):
        return r >= 0 and r < n and c >= 0 and c < n and matrix[r][c] == 0
    
    def find_solution():
        for r in range((n + 1) // 2):
            for c in range((n + 1) // 2):
                if matrix[r][c] == 0:
                    found = False
                    for num in list(counts.keys()):
                        if counts[num] >= 1:
                            
                            needed = 1
                            if r != n - 1 - r:
                                needed += 1
                            if c != n - 1 - c:
                                needed += 1
                            if r != n - 1 - r and c != n - 1 - c:
                                needed += 1
                                
                            if counts[num] >= needed:
                                
                                matrix[r][c] = num
                                matrix[n - 1 - r][c] = num
                                matrix[r][n - 1 - c] = num
                                matrix[n - 1 - r][n - 1 - c] = num
                                
                                counts[num] -= needed
                                
                                if counts[num] == 0:
                                    del counts[num]
                                
                                found = True
                                break
                    if not found:
                        return False
        return True
    
    if find_solution():
        print("YES")
        for row in matrix:
            print(*row)
    else:
        print("NO")
        

solve()