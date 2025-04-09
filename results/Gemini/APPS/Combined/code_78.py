def solve():
    n = int(input())
    s = input()
    len_s = len(s)
    mod = 10**9 + 7

    dp = {}

    def count_regular(length, balance, contains_s, index):
        if length == 0:
            return 1 if balance == 0 and contains_s else 0

        if (length, balance, contains_s, index) in dp:
            return dp[(length, balance, contains_s, index)]

        count = 0
        
        # Add '('
        if balance + 1 <= n:
            new_contains_s = contains_s
            new_index = index
            if not contains_s:
                if index < len_s and s[index] == '(':
                    new_index += 1
                else:
                    new_index = 0
                    if index < len_s and s[0] == '(':
                        new_index = 1
                if new_index == len_s:
                    new_contains_s = True
            count = (count + count_regular(length - 1, balance + 1, new_contains_s, new_index)) % mod

        # Add ')'
        if balance > 0:
            new_contains_s = contains_s
            new_index = index
            if not contains_s:
                if index < len_s and s[index] == ')':
                    new_index += 1
                else:
                    new_index = 0
                    if index < len_s and s[0] == ')':
                        new_index = 1
                if new_index == len_s:
                    new_contains_s = True
            count = (count + count_regular(length - 1, balance - 1, new_contains_s, new_index)) % mod

        dp[(length, balance, contains_s, index)] = count
        return count

    print(count_regular(2 * n, 0, False, 0))

solve()