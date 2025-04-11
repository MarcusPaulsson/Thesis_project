def generate_string(n, s, t):
    # Count of each character
    a_count = b_count = c_count = n
    
    # Create a list to hold the result
    res = []
    
    # Function to check if the last two characters form a forbidden substring
    def is_forbidden():
        return ''.join(res[-2:]) == s or ''.join(res[-2:]) == t
    
    # Build the result string
    while a_count > 0 or b_count > 0 or c_count > 0:
        for char in 'abc':
            if char == 'a' and a_count > 0:
                res.append(char)
                a_count -= 1
            elif char == 'b' and b_count > 0:
                res.append(char)
                b_count -= 1
            elif char == 'c' and c_count > 0:
                res.append(char)
                c_count -= 1
            
            # Check if the last two characters form a forbidden substring
            if is_forbidden():
                res.pop()  # Remove the last character added
                if char == 'a':
                    a_count += 1
                elif char == 'b':
                    b_count += 1
                elif char == 'c':
                    c_count += 1
                break  # Restart the loop to try adding a different character
        else:
            # If we went through all characters and couldn't add any, we are stuck
            print("NO")
            return

    # Join the result list into a string
    result_string = ''.join(res)
    
    # Check if we have a valid result
    if s in result_string or t in result_string:
        print("NO")
    else:
        print("YES")
        print(result_string)

# Input reading
n = int(input())
s = input().strip()
t = input().strip()

generate_string(n, s, t)