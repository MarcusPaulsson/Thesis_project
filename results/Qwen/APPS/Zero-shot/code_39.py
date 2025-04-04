def is_palindrome(s):
    return s == s[::-1]

def longest_non_palindrome_substring(s):
    max_length = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substring = s[i:j]
            if not is_palindrome(substring):
                max_length = max(max_length, len(substring))
    return max_length

s = input().strip()
print(longest_non_palindrome_substring(s))