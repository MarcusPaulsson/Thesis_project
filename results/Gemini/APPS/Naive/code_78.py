def solve():
    n = int(input())
    s = input()
    mod = 10**9 + 7
    len_s = len(s)
    
    dp = {}
    
    def count_regular(length, balance):
        if length == 0:
            return 1 if balance == 0 else 0
        if balance < 0:
            return 0
        
        if (length, balance) in dp:
            return dp[(length, balance)]
        
        res = (count_regular(length - 1, balance + 1) + count_regular(length - 1, balance - 1)) % mod
        dp[(length, balance)] = res
        return res

    def count_with_substring(n, s):
        total_regular = count_regular(2 * n, 0)
        
        def count_without_substring(n, s):
            
            def generate_bracket_sequences(length, balance, current_sequence, has_substring):
                if length == 0:
                    if balance == 0:
                        return 1 if has_substring else 0
                    else:
                        return 0
                
                count = 0
                
                # Add '('
                new_sequence_open = current_sequence + '('
                if not has_substring and s in new_sequence_open:
                    count = (count + generate_bracket_sequences(length - 1, balance + 1, new_sequence_open, True)) % mod
                elif has_substring:
                    count = (count + generate_bracket_sequences(length - 1, balance + 1, new_sequence_open, True)) % mod
                else:
                    count = (count + generate_bracket_sequences(length - 1, balance + 1, new_sequence_open, False)) % mod

                # Add ')'
                new_sequence_close = current_sequence + ')'
                if balance > 0:
                    if not has_substring and s in new_sequence_close:
                        count = (count + generate_bracket_sequences(length - 1, balance - 1, new_sequence_close, True)) % mod
                    elif has_substring:
                        count = (count + generate_bracket_sequences(length - 1, balance - 1, new_sequence_close, True)) % mod
                    else:
                        count = (count + generate_bracket_sequences(length - 1, balance - 1, new_sequence_close, False)) % mod
                
                return count
            
            return generate_bracket_sequences(2 * n, 0, "", False)
        
        without_substring = count_without_substring(n, s)
        return (total_regular - without_substring + mod) % mod

    if len_s > 2 * n:
        print(0)
    else:
        print(count_with_substring(n, s))

solve()