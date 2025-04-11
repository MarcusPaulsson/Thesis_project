def max_number_after_replacement(n, a, f):
    # Convert the function mapping to a list where index 0 corresponds to digit '1'
    f = [0] + f  # Adding a dummy value at index 0 for convenience

    # Convert the string of digits into a list of integers
    digits = list(map(int, a))
    
    # Initialize a flag to indicate if we have started replacing
    replacing = False
    
    # Iterate through the digits
    for i in range(n):
        current_digit = digits[i]
        mapped_digit = f[current_digit]
        
        if mapped_digit > current_digit:
            # Start replacing if the mapped digit is greater
            digits[i] = mapped_digit
            replacing = True
        elif mapped_digit < current_digit and replacing:
            # Stop replacing if we encounter a mapped digit less than the current digit
            break
    
    # Convert the list of digits back to a string
    return ''.join(map(str, digits))

# Example usage:
n = int(input())
a = input().strip()
f = list(map(int, input().strip().split()))
print(max_number_after_replacement(n, a, f))