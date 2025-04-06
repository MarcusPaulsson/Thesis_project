def is_palindrome(s):
    return s == s[::-1]

s = input().strip()

if not is_palindrome(s):
    print(len(s))
else:
    # Check if all characters are the same
    if all(c == s[0] for c in s):
        print(0)
    else:
        print(len(s) - 1)