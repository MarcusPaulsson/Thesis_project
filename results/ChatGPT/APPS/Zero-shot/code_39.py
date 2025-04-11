def is_palindrome(s):
    return s == s[::-1]

s = input().strip()

if not is_palindrome(s):
    print(len(s))
else:
    for length in range(len(s) - 1, 0, -1):
        for start in range(len(s) - length + 1):
            if not is_palindrome(s[start:start + length]):
                print(length)
                exit()
    print(0)