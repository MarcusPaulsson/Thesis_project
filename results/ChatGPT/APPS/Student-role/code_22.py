def is_s_palindrome(s):
    mirror_letters = {
        'A': 'A', 'b': 'd', 'C': 'C', 'd': 'b', 'E': 'E', 'H': 'H',
        'I': 'I', 'J': 'L', 'L': 'J', 'M': 'M', 'O': 'O', 'P': 'P',
        'Q': 'Q', 'R': 'R', 'S': 'S', 'T': 'T', 'U': 'U', 'V': 'V',
        'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': 'Z'
    }
    
    n = len(s)
    for i in range((n + 1) // 2):
        if s[i] not in mirror_letters or mirror_letters[s[i]] != s[n - 1 - i]:
            print("NIE")
            return
    print("TAK")

s = input().strip()
is_s_palindrome(s)