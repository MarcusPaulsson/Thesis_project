def is_s_palindrome(s):
    n = len(s)
    
    # Define the mirror characters
    mirror_chars = {
        'A': 'A', 'H': 'H', 'I': 'I', 'M': 'M', 'O': 'O', 'T': 'T', 
        'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 'o': 'o', 
        'v': 'v', 'x': 'x'
    }
    
    # Check for symmetry and mirror reflection
    for i in range((n + 1) // 2):
        left_char = s[i]
        right_char = s[n - 1 - i]
        
        if left_char not in mirror_chars or right_char not in mirror_chars:
            return "NIE"
        if mirror_chars[left_char] != right_char:
            return "NIE"
    
    return "TAK"

# Input
s = input().strip()
# Output
print(is_s_palindrome(s))