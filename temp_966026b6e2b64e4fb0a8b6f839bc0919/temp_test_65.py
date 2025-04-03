def solve():
    n = int(input())
    a = list(map(int, input().split()))

    dp = {}

    def calculate_min_skips(index, turn):
        if index == n:
            return 0

        if (index, turn) in dp:
            return dp[(index, turn)]

        if turn == 0: 
            ans = float('inf')
            
            ans = min(ans, a[index] + calculate_min_skips(index + 1, 1))
            
            if index + 1 < n:
                ans = min(ans, a[index] + a[index+1] + calculate_min_skips(index + 2, 1))

            dp[(index, turn)] = ans
            return ans
        else:
            
            ans = calculate_min_skips(index + 1, 0)
            if index + 1 < n:
                ans = min(ans, calculate_min_skips(index + 2, 0))
            
            dp[(index, turn)] = ans
            return ans

    print(calculate_min_skips(0, 0))

t = int(input())
for _ in range(t):
    solve()