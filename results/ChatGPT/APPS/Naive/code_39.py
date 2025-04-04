def is_palindrome(s):
    return s == s[::-1]

def longest_non_palindrome_substring(s):
    if not is_palindrome(s):
        return len(s)
    
    # Check if all characters are the same
    if all(c == s[0] for c in s):
        return 0
    
    # If it's a palindrome but not all characters are the same
    return len(s) - 1

# Input
s = input().strip()
# Output
print(longest_non_palindrome_substring(s))