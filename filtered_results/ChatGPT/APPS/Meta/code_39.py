def is_palindrome(s):
    return s == s[::-1]

def longest_non_palindrome_substring(s):
    n = len(s)
    
    # Check if the entire string is a palindrome
    if not is_palindrome(s):
        return n  # The whole string itself is the longest non-palindrome substring
    
    # Check for non-palindromic substrings by removing one character from either end
    for i in range(n):
        # Remove character from the start
        if not is_palindrome(s[i:]):
            return n - 1  # All substrings of this length will be non-palindromic
        
        # Remove character from the end
        if not is_palindrome(s[:n - i]):
            return n - 1  # All substrings of this length will be non-palindromic

    return 0  # If all substrings are palindromic

# Input
s = input().strip()
# Output
print(longest_non_palindrome_substring(s))