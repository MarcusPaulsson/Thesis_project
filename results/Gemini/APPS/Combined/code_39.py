def is_palindrome(s):
    return s == s[::-1]

def solve():
    s = input()
    n = len(s)
    max_len = 0
    for i in range(n):
        for j in range(i, n):
            sub = s[i:j+1]
            if not is_palindrome(sub):
                max_len = max(max_len, len(sub))
    print(max_len)

solve()