def solve():
    def count_classy(n):
        s = str(n)
        length = len(s)
        dp = {}

        def recurse(index, non_zero_count, tight):
            if index == length:
                return 1
            
            if (index, non_zero_count, tight) in dp:
                return dp[(index, non_zero_count, tight)]
            
            upper_bound = int(s[index]) if tight else 9
            count = 0
            
            for digit in range(upper_bound + 1):
                new_non_zero_count = non_zero_count + (digit != 0)
                new_tight = tight and (digit == upper_bound)
                
                if new_non_zero_count <= 3:
                    count += recurse(index + 1, new_non_zero_count, new_tight)
            
            dp[(index, non_zero_count, tight)] = count
            return count

        return recurse(0, 0, True)

    t = int(input())
    for _ in range(t):
        l, r = map(int, input().split())
        print(count_classy(r) - count_classy(l - 1))

solve()