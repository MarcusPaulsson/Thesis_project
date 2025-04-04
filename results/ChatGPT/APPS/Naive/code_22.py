def is_s_palindrome(s):
    mirror_chars = {'A': 'A', 'H': 'H', 'I': 'I', 'M': 'M', 'O': 'O', 'T': 'T', 
                    'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 
                    'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p', 'o': 'o', 'v': 'v', 'w': 'w', 'x': 'x'}
    
    n = len(s)
    for i in range((n + 1) // 2):
        left_char = s[i]
        right_char = s[n - 1 - i]
        
        if left_char not in mirror_chars or right_char not in mirror_chars:
            return "NIE"
        
        if mirror_chars[left_char] != right_char:
            return "NIE"
    
    return "TAK"

s = input().strip()
print(is_s_palindrome(s))