def is_s_palindrome(s):
    # Define the mirror mapping for characters
    mirror = {
        'A': 'A', 'B': '', 'C': '', 'D': '', 'E': '', 'F': '', 'G': '',
        'H': 'H', 'I': 'I', 'J': '', 'K': '', 'L': '', 'M': 'M', 'N': '',
        'O': 'O', 'P': '', 'Q': '', 'R': '', 'S': '', 'T': 'T', 'U': 'U',
        'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': '',
        'a': 'a', 'b': '', 'c': '', 'd': '', 'e': '', 'f': '', 'g': '',
        'h': 'h', 'i': 'i', 'j': '', 'k': '', 'l': '', 'm': 'm', 'n': '',
        'o': 'o', 'p': '', 'q': '', 'r': '', 's': '', 't': 't', 'u': 'u',
        'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y', 'z': ''
    }
    
    n = len(s)
    for i in range(n // 2):
        if mirror.get(s[i], '') != s[n - 1 - i] or mirror.get(s[n - 1 - i], '') != s[i]:
            return "NIE"
    
    return "TAK"

s = input().strip()
print(is_s_palindrome(s))