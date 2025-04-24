def solve():
    n = int(input())
    s = input()
    mod = 10**9 + 7
    len_s = len(s)

    dp = {}

    def count_regular_sequences(length, balance, found_s, kmp_state):
        if (length, balance, found_s, kmp_state) in dp:
            return dp[(length, balance, found_s, kmp_state)]

        if length == 2 * n:
            if balance == 0 and found_s:
                return 1
            else:
                return 0

        count = 0
        
        # Add '('
        if balance + 1 <= n:
            new_kmp_state = compute_kmp_state(kmp_table, kmp_state, '(')
            new_found_s = found_s or new_kmp_state == len_s
            count = (count + count_regular_sequences(length + 1, balance + 1, new_found_s, new_kmp_state)) % mod

        # Add ')'
        if balance > 0:
            new_kmp_state = compute_kmp_state(kmp_table, kmp_state, ')')
            new_found_s = found_s or new_kmp_state == len_s
            count = (count + count_regular_sequences(length + 1, balance - 1, new_found_s, new_kmp_state)) % mod

        dp[(length, balance, found_s, kmp_state)] = count
        return count

    def compute_kmp_table(pattern):
        length = len(pattern)
        table = [0] * length
        i = 1
        j = 0
        while i < length:
            if pattern[i] == pattern[j]:
                j += 1
                table[i] = j
                i += 1
            else:
                if j != 0:
                    j = table[j - 1]
                else:
                    i += 1
        return table

    def compute_kmp_state(table, state, char):
        while state > 0 and char != s[state]:
            state = table[state - 1]
        if char == s[state]:
            state += 1
        return state

    kmp_table = compute_kmp_table(s)
    result = count_regular_sequences(0, 0, False, 0)
    print(result)

solve()