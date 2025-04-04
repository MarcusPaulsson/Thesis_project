def max_possible_number(n, a, f):
    # Convert the input string to a list for easier modification
    a_list = list(a)
    
    # Flag to check if we have started changing digits
    started_changing = False
    
    # Iterate through each digit in the number
    for i in range(n):
        current_digit = int(a_list[i])
        # Check if we should change this digit
        if f[current_digit - 1] > current_digit:
            # If we haven't started changing, start now
            if not started_changing:
                started_changing = True
            # Replace the digit with its mapped value
            a_list[i] = str(f[current_digit - 1])
        elif f[current_digit - 1] < current_digit and started_changing:
            # If we started changing and encounter a digit that would decrease the number, stop changing
            break
    
    # Join the list back into a string and return
    return ''.join(a_list)

# Input reading
n = int(input().strip())
a = input().strip()
f = list(map(int, input().strip().split()))

# Get the result and print it
result = max_possible_number(n, a, f)
print(result)