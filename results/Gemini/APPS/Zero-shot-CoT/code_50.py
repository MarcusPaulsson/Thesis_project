def solve():
    n = int(input())
    a = list(map(int, input().split()))

    ans = float('inf')

    for left_eaten in range(n + 1):
        for right_eaten in range(n + 1):
            
            temp_a = a[:]
            
            left_start = n - 1
            right_start = n
            
            strawberry_count = 0
            blueberry_count = 0
            
            for i in range(left_start - left_eaten + 1, left_start + 1):
                if 0 <= i < 2 * n:
                    if temp_a[i] == 1:
                        strawberry_count += 1
                    else:
                        blueberry_count += 1
            
            for i in range(right_start, right_start + right_eaten):
                if 0 <= i < 2 * n:
                    if temp_a[i] == 1:
                        strawberry_count += 1
                    else:
                        blueberry_count += 1

            
            remaining_strawberry = 0
            remaining_blueberry = 0
            
            for i in range(2 * n):
                if i < n - left_eaten or i >= n + right_eaten:
                    if temp_a[i] == 1:
                        remaining_strawberry += 1
                    else:
                        remaining_blueberry += 1
                        
            if remaining_strawberry == remaining_blueberry:
                ans = min(ans, left_eaten + right_eaten)

    print(ans)

t = int(input())
for _ in range(t):
    solve()