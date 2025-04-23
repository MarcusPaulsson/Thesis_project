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
    # we can remove one character to create a non-palindrome substring
    return n - 1

# Input reading
s = input().strip()
# Output the result
print(longest_non_palindrome_substring(s))