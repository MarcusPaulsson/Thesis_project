def is_s_palindrome(s):
    # Define a mapping for mirror reflections
    mirror_map = {
        'A': 'A', 'b': 'd', 'd': 'b', 'H': 'H', 'I': 'I', 'M': 'M', 
        'O': 'O', 'p': 'q', 'q': 'p', 'T': 'T', 'U': 'U', 'v': 'v', 
        'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 'o': 'o', 'x': 'x'
    }
    
    n = len(s)
    for i in range((n + 1) // 2):
        if s[i] not in mirror_map or mirror_map[s[i]] != s[n - 1 - i]:
            print("NIE")
            return
    print("TAK")

s = input().strip()
is_s_palindrome(s)