def is_palindrome(s):
    return s == s[::-1]

def longest_non_palindrome_substring(s):
    n = len(s)
    
    # Check if the entire string is a palindrome
    if not is_palindrome(s):
        return n
    
    # Check if all characters are the same
    if s.count(s[0]) == n:
        return 0
    
    # The longest non-palindrome substring can be obtained by removing one character from either end
    return n - 1

# Read input
s = input().strip()
# Output the result
print(longest_non_palindrome_substring(s))