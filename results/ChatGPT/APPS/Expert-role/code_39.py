def is_palindrome(s):
    return s == s[::-1]

def longest_non_palindrome(s):
    n = len(s)
    
    # If the string itself is not a palindrome, return its length
    if not is_palindrome(s):
        return n
    
    # Check if all characters are the same
    if s.count(s[0]) == n:
        return 0
    
    # The longest non-palindrome substring will be of length n-1
    return n - 1

# Input
s = input().strip()
# Output
print(longest_non_palindrome(s))