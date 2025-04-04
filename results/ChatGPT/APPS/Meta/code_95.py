def generate_string(n, s, t):
    # Create the result list
    res = []
    
    # Count of each character
    count_a = n
    count_b = n
    count_c = n
    
    # Create a list of available characters
    chars = ['a', 'b', 'c']
    
    # Function to check if the last two characters form forbidden substrings
    def is_forbidden():
        return ''.join(res[-2:]) == s or ''.join(res[-2:]) == t
    
    # Start placing characters in the result
    while count_a > 0 or count_b > 0 or count_c > 0:
        for char in chars:
            if char == 'a' and count_a > 0:
                res.append(char)
                count_a -= 1
            elif char == 'b' and count_b > 0:
                res.append(char)
                count_b -= 1
            elif char == 'c' and count_c > 0:
                res.append(char)
                count_c -= 1
            
            # Check if the last two characters form forbidden substrings
            if is_forbidden():
                # If forbidden, backtrack the last character added
                res.pop()
                # Restore count for the character that was removed
                if char == 'a':
                    count_a += 1
                elif char == 'b':
                    count_b += 1
                elif char == 'c':
                    count_c += 1
                
            # Check if we have completed the string
            if len(res) == 3 * n:
                print("YES")
                print(''.join(res))
                return
            
    print("NO")

# Input reading
n = int(input())
s = input().strip()
t = input().strip()

# Generate the string
generate_string(n, s, t)