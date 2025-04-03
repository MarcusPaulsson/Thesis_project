def solve():
    n = int(input())
    a = list(map(int, input().split()))

    dp = {}

    def calculate_min_skips(index, turn):
        if index == n:
            return 0
        
        if (index, turn) in dp:
            return dp[(index, turn)]

        if turn == 0:  # Friend's turn
            ans = float('inf')
            
            # Kill one boss
            if a[index] == 1:
                ans = min(ans, 1 + calculate_min_skips(index + 1, 1))
            else:
                ans = min(ans, calculate_min_skips(index + 1, 1))
            
            # Kill two bosses
            if index + 1 < n:
                skips = 0
                if a[index] == 1:
                    skips += 1
                if a[index + 1] == 1:
                    skips += 1
                ans = min(ans, skips + calculate_min_skips(index + 2, 1))
            
            dp[(index, turn)] = ans
            return ans
        else:  # Your turn
            ans = float('inf')
            
            # Kill one boss
            ans = min(ans, calculate_min_skips(index + 1, 0))
            
            # Kill two bosses
            if index + 1 < n:
                ans = min(ans, calculate_min_skips(index + 2, 0))
            
            dp[(index, turn)] = ans
            return ans

    print(calculate_min_skips(0, 0))

t = int(input())
for _ in range(t):
    solve()