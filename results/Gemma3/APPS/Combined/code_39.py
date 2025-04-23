def is_palindrome(s):
    return s == s[::-1]

def solve():
    s = input()
    n = len(s)
    max_len = 0
    for l in range(n):
        for r in range(l, n):
            sub = s[l:r+1]
            if not is_palindrome(sub):
                max_len = max(max_len, len(sub))
    print(max_len)

solve()