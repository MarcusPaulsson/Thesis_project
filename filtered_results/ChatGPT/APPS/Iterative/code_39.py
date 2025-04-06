def is_palindrome(s):
    return s == s[::-1]

def longest_non_palindrome_substring(s):
    n = len(s)
    if n <= 1 or not is_palindrome(s):
        return n
    
    for length in range(n - 1, 0, -1):
        for start in range(n - length + 1):
            substring = s[start:start + length]
            if not is_palindrome(substring):
                return length
    
    return 0

if __name__ == "__main__":
    s = input().strip()
    print(longest_non_palindrome_substring(s))