def solve():
    n = int(input())
    s = input()
    mod = 10**9 + 7
    len_s = len(s)
    len_seq = 2 * n

    dp = {}

    def count_regular(index, balance, contains_s):
        if index == len_seq:
            if balance == 0 and contains_s:
                return 1
            else:
                return 0

        if (index, balance, contains_s) in dp:
            return dp[(index, balance, contains_s)]

        count = 0
        
        # Try adding '('
        new_contains_s = contains_s
        if not contains_s:
            if index < len_s and s[index] != '(':
                pass
            elif index >= len_s or s[index] == '(':
                count = (count + count_regular(index + 1, balance + 1, contains_s)) % mod
            else:
                pass
        else:
            count = (count + count_regular(index + 1, balance + 1, contains_s)) % mod
            
        # Try adding ')'
        new_contains_s = contains_s
        if not contains_s:
            if balance > 0:
                if index < len_s and s[index] != ')':
                    pass
                elif index >= len_s or s[index] == ')':
                    count = (count + count_regular(index + 1, balance - 1, contains_s)) % mod
                else:
                    pass
        else:
            if balance > 0:
                count = (count + count_regular(index + 1, balance - 1, contains_s)) % mod

        dp[(index, balance, contains_s)] = count

        return count

    def check_substring(seq, sub):
        for i in range(len(seq) - len(sub) + 1):
            if seq[i:i+len(sub)] == sub:
                return True
        return False

    def count_regular_optimized():
        dp = {}

        def solve_recursive(idx, balance, has_substring):
            if idx == 2 * n:
                if balance == 0 and has_substring:
                    return 1
                else:
                    return 0

            if (idx, balance, has_substring) in dp:
                return dp[(idx, balance, has_substring)]

            count = 0

            # Option 1: Add '('
            new_has_substring = has_substring
            if not has_substring and idx < len_s and s[idx] != '(':
                pass
            else:
                if not has_substring and idx < len_s and s[idx] == '(':
                    new_has_substring = (idx == len_s - 1)
                elif not has_substring and idx >= len_s:
                    pass
                count = (count + solve_recursive(idx + 1, balance + 1, new_has_substring)) % mod

            # Option 2: Add ')'
            if balance > 0:
                new_has_substring = has_substring
                if not has_substring and idx < len_s and s[idx] != ')':
                    pass
                else:
                    if not has_substring and idx < len_s and s[idx] == ')':
                        new_has_substring = (idx == len_s - 1)
                    elif not has_substring and idx >= len_s:
                        pass
                count = (count + solve_recursive(idx + 1, balance - 1, new_has_substring)) % mod

            dp[(idx, balance, has_substring)] = count
            return count

        return solve_recursive(0, 0, False)

    print(count_regular_optimized())

solve()