def is_palindrome(s):
    return s == s[::-1]

def longest_non_palindrome_substring(s):
    n = len(s)
    max_len = 0
    for i in range(n):
        for j in range(i, n):
            substring = s[i:j+1]
            if not is_palindrome(substring):
                max_len = max(max_len, len(substring))
    return max_len

if __name__ == "__main__":
    s = input()
    result = longest_non_palindrome_substring(s)
    print(result)