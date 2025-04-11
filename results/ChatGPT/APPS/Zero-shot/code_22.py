def is_s_palindrome(s):
    mirror_chars = {'A': 'A', 'b': 'd', 'd': 'b', 'H': 'H', 'I': 'I', 'M': 'M', 'O': 'O', 'p': 'q', 'q': 'p', 'R': 'R', 'S': 'S', 'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 'o': 'o', 'x': 'x'}
    
    n = len(s)
    for i in range((n + 1) // 2):
        if s[i] not in mirror_chars or s[n - 1 - i] != mirror_chars[s[i]]:
            print("NIE")
            return
    print("TAK")

s = input().strip()
is_s_palindrome(s)