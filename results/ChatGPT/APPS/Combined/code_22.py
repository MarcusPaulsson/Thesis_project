def is_s_palindrome(s: str) -> str:
    # Define a mapping of characters to their mirror counterparts
    mirror_map = {
        'A': 'A', 'b': 'd', 'd': 'b', 'H': 'H', 'I': 'I', 
        'M': 'M', 'O': 'O', 'o': 'o', 'p': 'q', 'q': 'p', 
        'T': 'T', 'U': 'U', 'v': 'v', 'W': 'W', 'X': 'X', 
        'Y': 'Y', 'Z': 'Z'
    }
    
    n = len(s)
    for i in range((n + 1) // 2):  # Check up to the middle of the string
        left_char = s[i]
        right_char = s[n - 1 - i]
        
        # Validate and check for mirror characters
        if (left_char not in mirror_map) or (right_char not in mirror_map) or (mirror_map[left_char] != right_char):
            return "NIE"
    
    return "TAK"

# Read input
s = input().strip()
# Print result
print(is_s_palindrome(s))