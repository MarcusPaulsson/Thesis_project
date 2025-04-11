def is_palindrome(s):
    return s == s[::-1]

s = input().strip()

if not is_palindrome(s):
    print(len(s))
else:
    # Check for the longest non-palindrome substring
    if len(set(s)) == 1:  # All characters are the same
        print(0)
    else:
        print(len(s) - 1)  # The longest non-palindrome substring will be of length len(s) - 1