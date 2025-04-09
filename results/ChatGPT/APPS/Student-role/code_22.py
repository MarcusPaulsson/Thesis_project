def is_s_palindrome(s):
    mirror = {
        'A': 'A', 'B': ' ', 'C': ' ', 'D': ' ', 'E': ' ', 'F': ' ', 'G': ' ', 'H': 'H',
        'I': 'I', 'J': ' ', 'K': ' ', 'L': ' ', 'M': 'M', 'N': ' ', 'O': 'O', 'P': ' ',
        'Q': ' ', 'R': ' ', 'S': ' ', 'T': 'T', 'U': 'U', 'V': ' ', 'W': 'W', 'X': 'X',
        'Y': ' ', 'Z': ' '
    }
    
    n = len(s)
    for i in range((n + 1) // 2):
        left = s[i]
        right = s[n - 1 - i]
        if mirror.get(left) != right:
            print("NIE")
            return
    print("TAK")

s = input().strip()
is_s_palindrome(s)