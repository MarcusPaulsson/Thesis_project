def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    counts = {}
    for x in a:
        counts[x] = counts.get(x, 0) + 1
    
    matrix = [[0] * n for _ in range(n)]
    
    for i in range(n // 2):
        for j in range(n // 2):
            found = False
            for num, count in list(counts.items()):
                if count >= 4:
                    matrix[i][j] = num
                    matrix[i][n - 1 - j] = num
                    matrix[n - 1 - i][j] = num
                    matrix[n - 1 - i][n - 1 - j] = num
                    counts[num] -= 4
                    if counts[num] == 0:
                        del counts[num]
                    found = True
                    break
            if not found:
                print("NO")
                return
    
    if n % 2 == 1:
        mid = n // 2
        for i in range(n // 2):
            found = False
            for num, count in list(counts.items()):
                if count >= 2:
                    matrix[i][mid] = num
                    matrix[n - 1 - i][mid] = num
                    counts[num] -= 2
                    if counts[num] == 0:
                        del counts[num]
                    found = True
                    break
            if not found:
                print("NO")
                return

        for j in range(n // 2):
            found = False
            for num, count in list(counts.items()):
                if count >= 2:
                    matrix[mid][j] = num
                    matrix[mid][n - 1 - j] = num
                    counts[num] -= 2
                    if counts[num] == 0:
                        del counts[num]
                    found = True
                    break
            if not found:
                print("NO")
                return
        
        found = False
        for num, count in list(counts.items()):
            if count >= 1:
                matrix[mid][mid] = num
                counts[num] -= 1
                if counts[num] == 0:
                    del counts[num]
                found = True
                break
        if not found:
            print("NO")
            return
    
    print("YES")
    for row in matrix:
        print(*row)

solve()