def is_palindrome(s):
    return s == s[::-1]

def longest_non_palindrome_substring(s):
    n = len(s)
    
    # Check if the entire string is a palindrome
    if not is_palindrome(s):
        return n
    
    # If the string is a palindrome, check for non-palindromic substrings
    for i in range(n):
        for j in range(i + 1, n):
            if not is_palindrome(s[i:j + 1]):
                return j - i + 1
    
    return 0

s = input().strip()
print(longest_non_palindrome_substring(s))