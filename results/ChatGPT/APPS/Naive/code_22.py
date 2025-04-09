def is_s_palindrome(s: str) -> str:
    mirror_chars = {
        'A': 'A', 'b': 'd', 'd': 'b', 'H': 'H', 'I': 'I', 'M': 'M',
        'O': 'O', 'p': 'q', 'q': 'p', 'T': 'T', 'U': 'U', 'v': 'v',
        'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 'o': 'o', 'x': 'x'
    }
    
    n = len(s)
    for i in range((n + 1) // 2):
        left_char = s[i]
        right_char = s[n - 1 - i]
        
        if left_char not in mirror_chars or right_char != mirror_chars[left_char]:
            return "NIE"
    
    return "TAK"

# Read input
input_string = input().strip()
# Output result
print(is_s_palindrome(input_string))