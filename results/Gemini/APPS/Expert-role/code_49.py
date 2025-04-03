def solve():
    def count_classy(n):
        s = str(n)
        length = len(s)
        
        dp = {}
        
        def recurse(idx, non_zero_count, is_tight):
            if idx == length:
                return 1
            
            if (idx, non_zero_count, is_tight) in dp:
                return dp[(idx, non_zero_count, is_tight)]
            
            ans = 0
            
            upper_bound = int(s[idx]) if is_tight else 9
            
            for digit in range(upper_bound + 1):
                new_non_zero_count = non_zero_count + (digit != 0)
                
                if new_non_zero_count <= 3:
                    new_is_tight = is_tight and (digit == int(s[idx]))
                    ans += recurse(idx + 1, new_non_zero_count, new_is_tight)
            
            dp[(idx, non_zero_count, is_tight)] = ans
            return ans
        
        return recurse(0, 0, True)
    
    t = int(input())
    for _ in range(t):
        l, r = map(int, input().split())
        print(count_classy(r) - count_classy(l - 1))

solve()