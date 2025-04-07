def is_s_palindrome(s):
    mirror_chars = {
        'A': 'A', 'b': 'd', 'd': 'b', 'H': 'H', 'I': 'I', 'M': 'M',
        'O': 'O', 'o': 'o', 'p': 'q', 'q': 'p', 'R': 'R', 'S': 'S',
        'T': 'T', 'U': 'U', 'v': 'v', 'V': 'V', 'W': 'W', 'x': 'x',
        'Y': 'Y'
    }
    
    n = len(s)
    for i in range((n + 1) // 2):
        left_char = s[i]
        right_char = s[n - 1 - i]
        
        if left_char not in mirror_chars or right_char != mirror_chars[left_char]:
            print("NIE")
            return
    print("TAK")

s = input().strip()
is_s_palindrome(s)