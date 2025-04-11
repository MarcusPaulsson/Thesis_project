def is_s_palindrome(s):
    mirror_chars = {
        'A': 'A', 'b': 'd', 'd': 'b', 'H': 'H', 'I': 'I', 'M': 'M',
        'O': 'O', 'p': 'q', 'q': 'p', 'T': 'T', 'U': 'U', 'v': 'v',
        'V': 'V', 'w': 'w', 'X': 'X', 'Y': 'Y', 'o': 'o', 'x': 'x'
    }
    
    n = len(s)
    for i in range((n + 1) // 2):
        if s[i] not in mirror_chars or mirror_chars[s[i]] != s[n - 1 - i]:
            return "NIE"
    return "TAK"

s = input().strip()
print(is_s_palindrome(s))