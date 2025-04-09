def is_palindrome(s):
    return s == s[::-1]

def longest_non_palindrome_substring(s):
    n = len(s)
    
    if not is_palindrome(s):
        return n
    
    for length in range(n - 1, 0, -1):
        for start in range(n - length + 1):
            if not is_palindrome(s[start:start + length]):
                return length
    
    return 0

s = input().strip()
print(longest_non_palindrome_substring(s))