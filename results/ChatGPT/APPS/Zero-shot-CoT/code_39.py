def is_palindrome(s):
    return s == s[::-1]

def longest_non_palindrome_substring(s):
    n = len(s)
    
    # If the entire string is not a palindrome, return its length
    if not is_palindrome(s):
        return n
    
    # Check for the longest non-palindrome substring
    for length in range(n - 1, 0, -1):  # Check lengths from n-1 to 1
        for start in range(n - length + 1):
            substring = s[start:start + length]
            if not is_palindrome(substring):
                return length
    
    return 0  # All substrings are palindromes

# Read input
s = input().strip()
# Output the result
print(longest_non_palindrome_substring(s))