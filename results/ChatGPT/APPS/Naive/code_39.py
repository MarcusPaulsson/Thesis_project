def is_palindrome(s):
    return s == s[::-1]

def longest_non_palindrome_substring(s):
    n = len(s)
    
    # If the entire string is not a palindrome, return its length
    if not is_palindrome(s):
        return n
    
    # If the entire string is a palindrome, check for non-palindrome substrings
    for i in range(n):
        for j in range(i + 1, n):
            substring = s[i:j + 1]
            if not is_palindrome(substring):
                return j - i + 1
    
    return 0

# Input
s = input().strip()
# Output
print(longest_non_palindrome_substring(s))