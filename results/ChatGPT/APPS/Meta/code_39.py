def is_palindrome(s):
    return s == s[::-1]

def longest_non_palindrome_substring(s):
    n = len(s)
    
    # Check if the entire string is a palindrome
    if not is_palindrome(s):
        return n
    
    # Check for the longest non-palindrome substring by removing one character from either end
    for i in range(n):
        if s[i] != s[0]:  # Check if removing the first character makes it non-palindrome
            return n - 1
        if s[i] != s[-1]:  # Check if removing the last character makes it non-palindrome
            return n - 1
    
    # If all characters are the same, return 0
    return 0

# Input
s = input().strip()
# Output
print(longest_non_palindrome_substring(s))