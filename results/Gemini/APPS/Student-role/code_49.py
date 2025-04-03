def solve():
    def count_classy(n):
        s = str(n)
        length = len(s)
        memo = {}

        def dp(idx, non_zero_count, tight):
            if idx == length:
                return 1
            
            if (idx, non_zero_count, tight) in memo:
                return memo[(idx, non_zero_count, tight)]
            
            ans = 0
            upper_bound = int(s[idx]) if tight else 9
            
            for digit in range(upper_bound + 1):
                new_non_zero_count = non_zero_count + (digit != 0)
                new_tight = tight and (digit == int(s[idx]))
                
                if new_non_zero_count <= 3:
                    ans += dp(idx + 1, new_non_zero_count, new_tight)
            
            memo[(idx, non_zero_count, tight)] = ans
            return ans

        return dp(0, 0, True)
    
    l, r = map(int, input().split())
    print(count_classy(r) - count_classy(l - 1))

t = int(input())
for _ in range(t):
    solve()