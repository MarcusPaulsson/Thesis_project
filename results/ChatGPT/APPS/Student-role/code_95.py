def generate_string(n, s, t):
    # Create a list to hold the result
    res = []
    
    # Count of each character
    count_a = n
    count_b = n
    count_c = n
    
    # Function to check if the last two characters form a forbidden substring
    def is_forbidden():
        if len(res) < 2:
            return False
        return ''.join(res[-2:]) in (s, t)
    
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
                # If forbidden, remove the last character and try the next one
                res.pop()
                if char == 'a':
                    count_a += 1
                elif char == 'b':
                    count_b += 1
                elif char == 'c':
                    count_c += 1
                break
        else:
            # If we went through all characters and didn't break, we are done
            break
    
    # Check if we have used all characters
    if count_a == 0 and count_b == 0 and count_c == 0:
        print("YES")
        print(''.join(res))
    else:
        print("NO")

# Input reading
n = int(input())
s = input().strip()
t = input().strip()

generate_string(n, s, t)