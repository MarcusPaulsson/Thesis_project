def is_palindrome(s):
    return s == s[::-1]

s = input().strip()

if not is_palindrome(s):
    print(len(s))
else:
    n = len(s)
    if s[0] != s[-1]:
        print(n)
    else:
        print(0)