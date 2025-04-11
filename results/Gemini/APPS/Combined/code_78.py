def solve():
    n = int(input())
    s = input()
    mod = 10**9 + 7
    len_s = len(s)

    def count_regular_sequences(n, s):
        count = 0
        
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

        def generate_sequences(current_seq, open_count, close_count):
            nonlocal count
            if len(current_seq) == 2 * n:
                if is_regular(current_seq) and s in current_seq:
                    count = (count + 1) % mod
                return

            if open_count < n:
                generate_sequences(current_seq + '(', open_count + 1, close_count)
            if close_count < open_count:
                generate_sequences(current_seq + ')', open_count, close_count + 1)

        generate_sequences("", 0, 0)
        return count

    
    dp = {}

    def count_regular_sequences_dp(length, balance, contains_s):
        if (length, balance, contains_s) in dp:
            return dp[(length, balance, contains_s)]

        if length == 2 * n:
            if balance == 0 and contains_s:
                return 1
            else:
                return 0

        if balance < 0:
            return 0

        res = 0
        
        # Add '('
        if balance < n:
            new_contains_s = contains_s
            temp_seq = ""
            if length < len_s:
                temp_seq = "(" + s[:length]
            else:
                temp_seq = current_seq = "("
                
            if not contains_s:
                if (temp_seq).endswith(s):
                    new_contains_s = True
            
            res = (res + count_regular_sequences_dp(length + 1, balance + 1, new_contains_s)) % mod

        # Add ')'
        new_contains_s = contains_s
        temp_seq = ""
        if length < len_s:
            temp_seq = ")" + s[:length]
        else:
            temp_seq = ")"
        
        if not contains_s:
            if (temp_seq).endswith(s):
                new_contains_s = True
        
        res = (res + count_regular_sequences_dp(length + 1, balance - 1, new_contains_s)) % mod

        dp[(length, balance, contains_s)] = res
        return res

    print(count_regular_sequences_dp(0, 0, False))

solve()