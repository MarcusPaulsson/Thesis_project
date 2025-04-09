def is_palindrome(s):
    return s == s[::-1]

s = input().strip()

# If the entire string is not a palindrome, return its length
if not is_palindrome(s):
    print(len(s))
else:
    # Check for the longest non-palindrome substring
    n = len(s)
    # If all characters are the same, return 0
    if s.count(s[0]) == n:
        print(0)
    else:
        # The longest non-palindrome substring can be at least n-1
        print(n - 1)