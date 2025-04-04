def construct_binary_string(a, b, x):
    # Start with the base pattern depending on x
    if x % 2 == 1:
        s = '01' * (x // 2) + '0' * (a - (x // 2)) + '1' * (b - (x // 2))
    else:
        s = '10' * (x // 2) + '0' * (a - (x // 2)) + '1' * (b - (x // 2))
    
    # Adjust the string to meet the exact counts of a and b
    if a > b:
        s = s.replace('0', '', a - (x // 2))
    else:
        s = s.replace('1', '', b - (x // 2))
    
    # Fill remaining characters
    while len(s) < a + b:
        if a > 0:
            s += '0'
            a -= 1
        if b > 0:
            s += '1'
            b -= 1
    
    return s

# Read input
a, b, x = map(int, input().split())
result = construct_binary_string(a, b, x)
print(result)