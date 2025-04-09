def is_palindrome(s):
    return s == s[::-1]

def longest_non_palindrome_substring(s):
    n = len(s)
    
    # If the entire string is not a palindrome, return its length
    if not is_palindrome(s):
        return n
    
    # Check if all characters in the string are the same
    if s.count(s[0]) == n:
        return 0
    
    # If the entire string is a palindrome, return n-1
    return n - 1

# Input
s = input().strip()
# Output
print(longest_non_palindrome_substring(s))