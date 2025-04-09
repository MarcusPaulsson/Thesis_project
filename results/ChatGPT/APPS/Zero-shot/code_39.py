def is_palindrome(s):
    return s == s[::-1]

s = input().strip()

if not is_palindrome(s):
    print(len(s))
else:
    # Check for any non-palindrome substring of length > 1
    if len(set(s)) == 1:
        print(0)
    else:
        print(len(s) - 1)