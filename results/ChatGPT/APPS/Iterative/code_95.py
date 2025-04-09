def generate_string(n, s, t):
    # Check for impossible cases
    if (s[0] == t[0] or s[1] == t[1]) and (s[0] == s[1] or t[0] == t[1]):
        return "NO"
    
    # Initialize counts for 'a', 'b', and 'c'
    count = {'a': n, 'b': n, 'c': n}
    
    # Start building the result string
    result = []
    
    # Function to append a character while ensuring no invalid substrings
    def append_char():
        for char in 'abc':
            if count[char] > 0:
                # Check the last two characters in the result to avoid forbidden substrings
                if len(result) < 2 or result[-1] != char or result[-2] != char:
                    return char
        return None
    
    # Construct the result string
    for _ in range(3 * n):
        char = append_char()
        if char is None:
            return "NO"
        result.append(char)
        count[char] -= 1
    
    # Final check for forbidden substrings
    for i in range(len(result) - 1):
        if ''.join(result[i:i+2]) == s or ''.join(result[i:i+2]) == t:
            return "NO"
    
    return "YES", ''.join(result)

n = int(input())
s = input().strip()
t = input().strip()

result = generate_string(n, s, t)
if result == "NO":
    print(result)
else:
    print(result[0])
    print(result[1])