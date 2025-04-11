def is_rotation(A, B):
    # Convert integers to strings
    str_A = str(A)
    str_B = str(B)
    
    # Store the count of digits
    dig1 = len(str_A)
    dig2 = len(str_B)
    
    # If the number of digits is not the same, they cannot be rotations
    if dig1 != dig2:
        return False
    
    # Store the first digit and its position
    first_digit = str_A[0]
    position = 0
    
    # Rotate the digits of A
    for i in range(dig1):
        # Rotate the string
        rotated = str_A[i:] + str_A[:i]
        if rotated == str_B:
            return True
    
    return False

# Driver code
A = 1234
B = 3412
print(is_rotation(A, B))  # Example usage