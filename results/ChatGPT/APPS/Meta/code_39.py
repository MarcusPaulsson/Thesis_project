def is_palindrome(s):
    return s == s[::-1]

def longest_non_palindrome_substring(s):
    n = len(s)
    
    # If the string itself is not a palindrome
    if not is_palindrome(s):
        return n
    
    # Check for non-palindrome by removing one character from either end
    for i in range(n):
        if s[i] != s[0]:  # Remove the first character
            return n - 1
        if s[i] != s[-1]:  # Remove the last character
            return n - 1
    
    # If all characters are the same, there is no valid non-palindrome substring
    return 0

# Input
s = input().strip()
# Output
print(longest_non_palindrome_substring(s))