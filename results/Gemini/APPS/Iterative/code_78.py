def solve():
    n = int(input())
    s = input()
    mod = 10**9 + 7
    
    def is_regular(seq):
        balance = 0
        for char in seq:
            if char == '(':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False
        return balance == 0

    def count_sequences(n, s):
        count = 0
        for i in range(1 << (2 * n)):
            seq = ""
            for j in range(2 * n):
                if (i >> j) & 1:
                    seq += "("
                else:
                    seq += ")"
            
            if is_regular(seq) and s in seq:
                count += 1
        return count % mod

    #print(count_sequences(n, s))
    
    
    def count_regular_bracket_sequences(n, sub):
        m = len(sub)
        dp = {}
        
        def solve_recursive(index, balance, contains_sub):
            if (index, balance, contains_sub) in dp:
                return dp[(index, balance, contains_sub)]
            
            if index == 2 * n:
                if balance == 0 and contains_sub:
                    return 1
                else:
                    return 0
            
            count = 0
            
            # Option 1: Add '('
            new_balance = balance + 1
            new_contains_sub = contains_sub
            
            temp_seq = "("
            if index-m+1 >= 0:
                temp_seq = ""
                for k in range(index-m+1, index):
                    if (i >> k) & 1:
                        temp_seq += "("
                    else:
                        temp_seq += ")"
                temp_seq += "("
            
            if sub in temp_seq:
                new_contains_sub = True
            
            if new_balance <= n:
                
                
                i = 0
                
                count = (count + solve_recursive(index + 1, new_balance, contains_sub or (temp_seq.endswith(sub) and len(temp_seq) >= len(sub)))) % mod

                
            # Option 2: Add ')'
            new_balance = balance - 1
            new_contains_sub = contains_sub
            
            temp_seq = ")"
            if index-m+1 >= 0:
                temp_seq = ""
                for k in range(index-m+1, index):
                    if (i >> k) & 1:
                        temp_seq += "("
                    else:
                        temp_seq += ")"
                temp_seq += ")"
            
            
            if sub in temp_seq:
                new_contains_sub = True
            
            if new_balance >= 0:

                i = 0
                
                
                count = (count + solve_recursive(index + 1, new_balance, contains_sub or (temp_seq.endswith(sub) and len(temp_seq) >= len(sub)))) % mod
            
            
            dp[(index, balance, contains_sub)] = count
            return count
        
        
        i = 0
        print(solve_recursive(0, 0, False))
        
        
    count_regular_bracket_sequences(n, s)

solve()