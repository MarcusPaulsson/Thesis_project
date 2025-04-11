def is_palindrome(s):
    return s == s[::-1]

def longest_non_palindrome_substring(s):
    n = len(s)
    
    # If the entire string is not a palindrome, return its length
    if not is_palindrome(s):
        return n
    
    # Check for the longest non-palindrome substring by removing one character
    for i in range(n):
        if not is_palindrome(s[:i] + s[i+1:]):
            return n - 1
    
    # If all characters are the same, return 0
    return 0

# Input
s = input().strip()
# Output
print(longest_non_palindrome_substring(s))