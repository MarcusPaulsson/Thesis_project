def generate_string(n, s, t):
    # Count of each character
    count_a = count_b = count_c = n
    
    # Create a list to build the result string
    res = []
    
    # Function to check if the last two characters form a forbidden substring
    def is_forbidden():
        return ''.join(res[-2:]) == s or ''.join(res[-2:]) == t
    
    # Try to build the result string
    for _ in range(3 * n):
        for char in 'abc':
            if (char == 'a' and count_a > 0) or (char == 'b' and count_b > 0) or (char == 'c' and count_c > 0):
                res.append(char)
                if char == 'a':
                    count_a -= 1
                elif char == 'b':
                    count_b -= 1
                else:
                    count_c -= 1
                
                if is_forbidden():
                    res.pop()  # Remove the last character if it forms a forbidden substring
                    if char == 'a':
                        count_a += 1
                    elif char == 'b':
                        count_b += 1
                    else:
                        count_c += 1
                else:
                    break
        else:
            # If we couldn't add any character, it's impossible
            print("NO")
            return
    
    print("YES")
    print(''.join(res))

# Read input
n = int(input())
s = input().strip()
t = input().strip()

generate_string(n, s, t)