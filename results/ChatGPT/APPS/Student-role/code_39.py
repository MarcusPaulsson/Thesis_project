def is_palindrome(s):
    return s == s[::-1]

s = input().strip()

if not is_palindrome(s):
    print(len(s))
else:
    # Check for the longest non-palindrome substring
    n = len(s)
    for length in range(n - 1, 0, -1):
        for start in range(n - length + 1):
            substring = s[start:start + length]
            if not is_palindrome(substring):
                print(length)
                exit()
    print(0)