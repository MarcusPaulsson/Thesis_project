def solve():
    n = int(input())
    s = input()
    mod = 10**9 + 7
    len_s = len(s)

    dp = {}

    def count_regular_sequences(length, balance, contains_s):
        if length == 2 * n:
            if balance == 0 and contains_s:
                return 1
            else:
                return 0

        if (length, balance, contains_s) in dp:
            return dp[(length, balance, contains_s)]

        count = 0
        
        # Add '('
        if balance + 1 <= n:
            new_contains_s = contains_s
            if not contains_s:
                new_seq = ""
                if length > 0:
                    new_seq = current_seq + '('
                else:
                    new_seq = '('
                
                if len(new_seq) >= len_s and new_seq[len(new_seq) - len_s:] == s:
                    new_contains_s = True
            
            count = (count + count_regular_sequences(length + 1, balance + 1, contains_s or (len(current_seq + '(') >= len_s and (current_seq + '(')[len(current_seq + '(') - len_s:] == s))) % mod

        # Add ')'
        if balance > 0:
            new_contains_s = contains_s
            if not contains_s:
                new_seq = ""
                if length > 0:
                    new_seq = current_seq + ')'
                else:
                    new_seq = ')'
                
                if len(new_seq) >= len_s and new_seq[len(new_seq) - len_s:] == s:
                    new_contains_s = True
            
            count = (count + count_regular_sequences(length + 1, balance - 1, contains_s or (len(current_seq + ')') >= len_s and (current_seq + ')')[len(current_seq + ')') - len_s:] == s))) % mod

        dp[(length, balance, contains_s)] = count
        return count

    current_seq = ""
    dp = {}
    result = count_regular_sequences(0, 0, False)
    print(result)

solve()