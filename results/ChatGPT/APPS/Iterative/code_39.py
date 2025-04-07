def is_palindrome(s):
    return s == s[::-1]

s = input().strip()

if not is_palindrome(s):
    print(len(s))
else:
    # Check for the longest non-palindromic substring
    # If all characters are the same, then all substrings are palindromes
    if len(set(s)) == 1:
        print(0)
    else:
        # The longest non-palindromic substring will be the entire string minus one character
        print(len(s) - 1)