def is_s_palindrome(s):
    mirror_chars = {'A': 'A', 'b': 'd', 'd': 'b', 'H': 'H', 'I': 'I', 'M': 'M', 'O': 'O', 'o': 'o', 'p': 'q', 'q': 'p', 'R': 'R', 'S': 'S', 'T': 'T', 'U': 'U', 'v': 'v', 'V': 'V', 'W': 'W', 'x': 'x', 'Y': 'Y'}
    
    n = len(s)
    for i in range((n + 1) // 2):
        if s[i] not in mirror_chars or s[n - 1 - i] not in mirror_chars:
            return "NIE"
        if mirror_chars[s[i]] != s[n - 1 - i]:
            return "NIE"
    
    return "TAK"

s = input().strip()
print(is_s_palindrome(s))