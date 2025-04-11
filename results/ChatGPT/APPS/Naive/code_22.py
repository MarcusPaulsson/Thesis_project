def is_s_palindrome(s):
    # Define a mapping of characters to their mirror counterparts
    mirror_map = {
        'A': 'A', 'b': 'd', 'd': 'b', 'H': 'H', 'I': 'I', 'M': 'M',
        'O': 'O', 'p': 'q', 'q': 'p', 'R': 'R', 'S': 'S', 'T': 'T',
        'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 'o': 'o',
        'x': 'x'
    }

    n = len(s)
    for i in range((n + 1) // 2):
        left_char = s[i]
        right_char = s[n - 1 - i]
        
        # Check if the characters are mirror images
        if left_char not in mirror_map or mirror_map[left_char] != right_char:
            print("NIE")
            return
    
    print("TAK")

# Read input
s = input().strip()
is_s_palindrome(s)