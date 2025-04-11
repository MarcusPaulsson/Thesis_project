def is_palindrome(s):
    return s == s[::-1]

s = input().strip()

if not is_palindrome(s):
    print(len(s))
else:
    # Check for the longest non-palindrome substring
    n = len(s)
    # If all characters are the same, return 0
    if s.count(s[0]) == n:
        print(0)
    else:
        print(n - 1)