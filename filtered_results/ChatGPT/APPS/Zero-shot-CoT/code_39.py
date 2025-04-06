def is_palindrome(s):
    return s == s[::-1]

def longest_non_palindrome_substring(s):
    n = len(s)
    
    if not is_palindrome(s):
        return n
    
    # Check if all characters are the same
    if s == s[0] * n:
        return 0
    
    # If the whole string is a palindrome but not all characters are the same,
    # then the longest non-palindrome substring can be obtained by removing one character
    return n - 1

s = input().strip()
print(longest_non_palindrome_substring(s))