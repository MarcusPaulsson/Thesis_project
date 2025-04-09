def is_s_palindrome(s):
    mirror = {
        'A': 'A', 'b': 'd', 'd': 'b', 'H': 'H', 'I': 'I', 'M': 'M', 
        'O': 'O', 'p': 'q', 'q': 'p', 'R': 'R', 'S': 'S', 'T': 'T', 
        'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 'o': 'o', 
        'x': 'x'
    }
    
    n = len(s)
    for i in range((n + 1) // 2):
        if mirror.get(s[i], None) != s[n - 1 - i]:
            return "NIE"
    return "TAK"

s = input().strip()
print(is_s_palindrome(s))