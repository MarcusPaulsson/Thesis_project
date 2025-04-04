def is_s_palindrome(s):
    # Define the mirror pairs
    mirror_pairs = {
        'A': 'A', 'b': 'd', 'd': 'b', 'H': 'H', 'I': 'I', 'M': 'M',
        'O': 'O', 'p': 'q', 'q': 'p', 'R': 'R', 'S': 'S', 'T': 'T',
        'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': 'Z',
        'o': 'o', 'x': 'x'
    }
    
    n = len(s)
    for i in range((n + 1) // 2):
        left_char = s[i]
        right_char = s[n - 1 - i]
        
        if left_char not in mirror_pairs or mirror_pairs[left_char] != right_char:
            print("NIE")
            return
    
    print("TAK")

# Read input
s = input().strip()
is_s_palindrome(s)