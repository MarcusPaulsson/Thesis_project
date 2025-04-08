def is_palindrome(s):
    return s == s[::-1]

def longest_non_palindrome_substring(s):
    n = len(s)
    
    # Check if the entire string is a palindrome
    if not is_palindrome(s):
        return n
    
    # Check if all characters in the string are the same
    if all(char == s[0] for char in s):
        return 0
    
    # If the string is a palindrome but not all characters are the same,
    # the longest non-palindrome substring can be obtained by removing
    # either the first or the last character.
    return n - 1

# Read input
s = input().strip()
# Output the result
print(longest_non_palindrome_substring(s))