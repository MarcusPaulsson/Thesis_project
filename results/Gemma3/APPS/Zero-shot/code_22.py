def is_s_palindrome(s):
    n = len(s)
    mirror = {'A': 'A', 'H': 'H', 'I': 'I', 'M': 'M', 'O': 'O', 'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y',
              'b': 'd', 'd': 'b', 'o': 'o', 'p': 'q', 'q': 'p', 'v': 'v', 'w': 'w', 'x': 'x'}
    
    for i in range(n // 2):
        if s[i] not in mirror or s[n - 1 - i] not in mirror or mirror[s[i]] != s[n - 1 - i]:
            return False
    
    if n % 2 == 1:
        if s[n // 2] not in mirror or mirror[s[n // 2]] != s[n // 2]:
            return False
    
    return True

s = input()
if is_s_palindrome(s):
    print("TAK")
else:
    print("NIE")