def max_number_after_replacement(n, a, f):
    # Convert the function mapping to a list for easier access
    f = [0] + f  # f[0] is unused, f[1] to f[9] are used
    
    # Convert the string a into a list of characters for easier manipulation
    a_list = list(a)
    
    # Flag to indicate if we have started replacing
    replacing = False
    
    for i in range(n):
        current_digit = int(a_list[i])
        mapped_digit = f[current_digit]
        
        # If we haven't started replacing and the mapped digit is greater, start replacing
        if not replacing and mapped_digit > current_digit:
            replacing = True
        
        # If we are in the replacing mode, replace the digit
        if replacing:
            if mapped_digit >= current_digit:
                a_list[i] = str(mapped_digit)
            else:
                # Stop replacing if the mapped digit is less than the current digit
                break
    
    # Join the list back into a string and return the result
    return ''.join(a_list)

# Input reading
n = int(input().strip())
a = input().strip()
f = list(map(int, input().strip().split()))

# Get the result and print it
result = max_number_after_replacement(n, a, f)
print(result)