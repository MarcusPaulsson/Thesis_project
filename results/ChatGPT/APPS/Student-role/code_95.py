def generate_string(n, s, t):
    # Create a list to hold the result
    res = []
    
    # Count of characters
    count_a = n
    count_b = n
    count_c = n
    
    # Function to check if the last two characters form a forbidden substring
    def is_forbidden():
        if len(res) < 2:
            return False
        return ''.join(res[-2:]) == s or ''.join(res[-2:]) == t
    
    # Build the result string
    while count_a > 0 or count_b > 0 or count_c > 0:
        for char in 'abc':
            if char == 'a' and count_a > 0:
                res.append('a')
                count_a -= 1
            elif char == 'b' and count_b > 0:
                res.append('b')
                count_b -= 1
            elif char == 'c' and count_c > 0:
                res.append('c')
                count_c -= 1
            
            # Check if the last two characters form a forbidden substring
            if is_forbidden():
                res.pop()  # Remove the last character
                if char == 'a':
                    count_a += 1
                elif char == 'b':
                    count_b += 1
                elif char == 'c':
                    count_c += 1
                break  # Restart the loop to try the next character
    
    # Join the list into a string
    result_string = ''.join(res)
    
    # Check if we have the right length
    if len(result_string) == 3 * n:
        print("YES")
        print(result_string)
    else:
        print("NO")

# Input reading
n = int(input().strip())
s = input().strip()
t = input().strip()

generate_string(n, s, t)