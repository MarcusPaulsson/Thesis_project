def is_s_palindrome(s):
    mirror_chars = {'A': 'A', 'H': 'H', 'I': 'I', 'M': 'M', 'O': 'O', 'T': 'T', 'U': 'U', 
                    'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p'}
    
    n = len(s)
    for i in range((n + 1) // 2):
        if s[i] not in mirror_chars or mirror_chars[s[i]] != s[n - 1 - i]:
            print("NIE")
            return
    print("TAK")

s = input().strip()
is_s_palindrome(s)