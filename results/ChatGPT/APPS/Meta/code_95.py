def generate_string(n, s, t):
    # Create a base string with n 'a's, n 'b's, and n 'c's
    base = 'a' * n + 'b' * n + 'c' * n
    
    # Check if the strings s or t can be formed
    # We need to avoid generating those substrings
    for i in range(0, len(base) - 1):
        if base[i:i+2] == s or base[i:i+2] == t:
            return "NO"
    
    # Now we will create the result while avoiding both substrings
    res = []
    count_a = count_b = count_c = n
    
    # Create a list of characters
    chars = ['a', 'b', 'c']
    
    while count_a > 0 or count_b > 0 or count_c > 0:
        for char in chars:
            if char == 'a' and count_a > 0:
                if len(res) >= 1 and (res[-1] == 'a' or (len(res) >= 1 and res[-1] + char in (s, t))):
                    continue
                res.append(char)
                count_a -= 1
            elif char == 'b' and count_b > 0:
                if len(res) >= 1 and (res[-1] == 'b' or (len(res) >= 1 and res[-1] + char in (s, t))):
                    continue
                res.append(char)
                count_b -= 1
            elif char == 'c' and count_c > 0:
                if len(res) >= 1 and (res[-1] == 'c' or (len(res) >= 1 and res[-1] + char in (s, t))):
                    continue
                res.append(char)
                count_c -= 1
    
    # Join the result list to form the final string
    result_string = ''.join(res)
    
    # Final check for substrings
    for i in range(len(result_string) - 1):
        if result_string[i:i + 2] == s or result_string[i:i + 2] == t:
            return "NO"
    
    return "YES\n" + result_string

# Input reading
n = int(input())
s = input().strip()
t = input().strip()

# Generate the string and print the result
print(generate_string(n, s, t))