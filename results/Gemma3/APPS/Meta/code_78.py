def solve():
    n = int(input())
    s = input()
    
    MOD = 10**9 + 7
    
    def is_regular(seq):
        balance = 0
        for char in seq:
            if char == '(':
                balance += 1
            elif char == ')':
                balance -= 1
            if balance < 0:
                return False
        return balance == 0
    
    def catalan(n):
        if n == 0:
            return 1
        
        dp = [0] * (n + 1)
        dp[0] = 1
        
        for i in range(1, n + 1):
            for j in range(i):
                dp[i] = (dp[i] + (dp[j] * dp[i - 1 - j]) % MOD) % MOD
        
        return dp[n]
    
    count = 0
    
    import itertools
    
    for seq in itertools.product(['(', ')'], repeat=2 * n):
        seq_str = "".join(seq)
        
        if is_regular(seq_str) and s in seq_str:
            count = (count + 1) % MOD
            
    print(count)

solve()