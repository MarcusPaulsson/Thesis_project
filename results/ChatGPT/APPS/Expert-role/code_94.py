a, b, x = map(int, input().split())

# Determine how many transitions we need to create.
# Each transition requires at least one '0' and one '1'.
# We need to ensure we have enough to satisfy the request.
if x % 2 == 0:
    # Even number of transitions
    zeros = a
    ones = b
    s = []
    
    # Start with a 0 or 1 based on availability and x
    start_with_one = ones >= zeros
    if start_with_one:
        s.append('1')
        ones -= 1
    else:
        s.append('0')
        zeros -= 1
    
    for i in range(x // 2):
        if start_with_one:
            s.append('0')
            s.append('1')
            zeros -= 1
            ones -= 1
        else:
            s.append('1')
            s.append('0')
            ones -= 1
            zeros -= 1
    
    # Now we add the remaining characters
    if start_with_one:
        s += ['1'] * ones + ['0'] * zeros
    else:
        s += ['0'] * zeros + ['1'] * ones

else:
    # Odd number of transitions
    if a < b:
        s = ['0']  # start with 0, then alternate
        zeros = a - 1
        ones = b
    else:
        s = ['1']  # start with 1, then alternate
        ones = b - 1
        zeros = a
    
    for i in range(x // 2):
        s.append('1' if s[-1] == '0' else '0')
        if s[-1] == '1':
            ones -= 1
        else:
            zeros -= 1
    
    # Add one more transition
    s.append('1' if s[-1] == '0' else '0')
    if s[-1] == '1':
        ones -= 1
    else:
        zeros -= 1
    
    # Now add the remaining characters
    s += ['1'] * ones + ['0'] * zeros

print(''.join(s))