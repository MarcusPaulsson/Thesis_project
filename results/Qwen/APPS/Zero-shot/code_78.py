MOD = 10**9 + 7

def catalan(n):
    if n <= 1:
        return 1
    res_num = 1
    res_den = 1
    for i in range(2, n + 1):
        res_num *= (n + i)
        res_den *= i
    return res_num // res_den % MOD

def count_sequences(n, s):
    count = 0
    for i in range(n - len(s) + 1):
        left = s[:i]
        right = s[i + len(s):]
        left_count = catalan(left.count('(') - left.count(')'))
        right_count = catalan(right.count('(') - right.count(')'))
        if left_count == 0 or right_count == 0:
            continue
        middle = s[i:i + len(s)]
        if middle.count('(') >= middle.count(')'):
            count += left_count * right_count
            count %= MOD
    return count

n = int(input())
s = input()
print(count_sequences(n, s))