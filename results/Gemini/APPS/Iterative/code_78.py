def solve():
    n = int(input())
    s = input()
    mod = 10**9 + 7
    len_s = len(s)
    
    dp = {}
    
    def count_regular_sequences(index, balance, contains_s):
        if index == 2 * n:
            if balance == 0 and contains_s:
                return 1
            else:
                return 0
        
        if (index, balance, contains_s) in dp:
            return dp[(index, balance, contains_s)]
        
        count = 0
        
        # Add '('
        if balance + 1 <= n:
            new_contains_s = contains_s
            if not contains_s:
                if index < len_s and s[index] == '(':
                    
                    match = True
                    for i in range(min(len_s, 2*n - index)):
                        if index + i >= 2*n or s[i] != '(' if i == 0 else s[index+i] != s[i]:
                            match = False
                            break
                    if index + len_s <= 2*n and match:
                        new_contains_s = True
                elif index >= len_s:
                    new_contains_s = True
            
            count = (count + count_regular_sequences(index + 1, balance + 1, new_contains_s)) % mod
        
        # Add ')'
        if balance > 0:
            new_contains_s = contains_s
            if not contains_s:
                if index < len_s and s[index] == ')':
                    match = True
                    for i in range(min(len_s, 2*n - index)):
                        if index + i >= 2*n or s[i] != ')' if i == 0 else s[index+i] != s[i]:
                            match = False
                            break
                    if index + len_s <= 2*n and match:
                        new_contains_s = True
                elif index >= len_s:
                    new_contains_s = True
            
            count = (count + count_regular_sequences(index + 1, balance - 1, new_contains_s)) % mod
        
        dp[(index, balance, contains_s)] = count
        return count
    
    print(count_regular_sequences(0, 0, False))

solve()