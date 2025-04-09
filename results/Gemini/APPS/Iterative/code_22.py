def is_s_palindrome(s):
    mirrors = {
        'b': 'd', 'd': 'b',
        'p': 'q', 'q': 'p',
        'o': 'o', 'x': 'x',
        'v': 'v', 'w': 'w',
        'A': 'A', 'H': 'H',
        'I': 'I', 'M': 'M',
        'O': 'O', 'T': 'T',
        'U': 'U', 'V': 'V',
        'W': 'W', 'X': 'X',
        'Y': 'Y'
    }
    
    n = len(s)
    for i in range(n // 2):
        if s[i] not in mirrors or mirrors.get(s[i]) != s[n - 1 - i]:
            return "NIE"
    
    if n % 2 == 1:
        if s[n // 2] not in mirrors or mirrors.get(s[n // 2]) != s[n // 2]:
            return "NIE"
    
    return "TAK"

s = input()
print(is_s_palindrome(s))