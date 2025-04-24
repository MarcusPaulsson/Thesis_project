def solve():
    n, m, k = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    
    max_sum = 0
    
    for i in range(1 << m):
        if bin(i).count('1') <= m // 2:
            current_sum = 0
            for row in a:
                row_sum = 0
                for j in range(m):
                    if (i >> j) & 1:
                        row_sum += row[j]
                current_sum += row_sum
            
            if current_sum % k == 0:
                max_sum = max(max_sum, current_sum)
    
    print(max_sum)

solve()