def is_s_palindrome(s):
    mirror_map = {
        'A': 'A', 'H': 'H', 'I': 'I', 'M': 'M', 'O': 'O', 
        'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 
        'Y': 'Y', 'o': 'o', 'v': 'v', 'w': 'w', 'x': 'x'
    }
    
    n = len(s)
    for i in range((n + 1) // 2):
        if s[i] not in mirror_map or s[n - 1 - i] not in mirror_map:
            return "NIE"
        if mirror_map[s[i]] != s[n - 1 - i]:
            return "NIE"
    
    return "TAK"

s = input().strip()
print(is_s_palindrome(s))