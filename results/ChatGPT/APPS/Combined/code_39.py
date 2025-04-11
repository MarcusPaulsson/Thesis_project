def is_palindrome(s):
    return s == s[::-1]

def longest_non_palindrome_substring(s):
    n = len(s)
    
    # If the entire string is not a palindrome, return its length
    if not is_palindrome(s):
        return n
    
    # Check if all characters are the same
    if s.count(s[0]) == n:
        return 0
    
    # If the string is a palindrome but not all characters are the same,
    # the longest non-palindrome substring can be obtained by removing
    # one character from either end.
    return n - 1

# Input
s = input().strip()
# Output
print(longest_non_palindrome_substring(s))