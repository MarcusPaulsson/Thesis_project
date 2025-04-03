def is_palindrome(s):
    return s == s[::-1]

s = input().strip()

if not is_palindrome(s):
    print(len(s))
else:
    # Check for the longest non-palindromic substring
    for i in range(len(s)):
        for j in range(len(s), i, -1):
            if not is_palindrome(s[i:j]):
                print(j - i)
                exit()
    print(0)