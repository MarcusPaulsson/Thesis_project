def construct_binary_string(a, b, x):
    # Initialize an empty string
    s = []
    
    # Determine which character to start with based on the number of 0s and 1s
    if a > b:
        start = '0'
    else:
        start = '1'
    
    # We need to create x transitions
    # If x is odd, we will finish with the opposite character
    transition = 0
    while a > 0 or b > 0:
        if (transition % 2 == 0 and a > 0) or b == 0:
            s.append('0')
            a -= 1
        else:
            s.append('1')
            b -= 1
        
        # Increase the transition count
        if a > 0 and b > 0:
            transition += 1
    
    # If we have used all transitions but still have characters left, fill them
    while a > 0:
        s.append('0')
        a -= 1
    while b > 0:
        s.append('1')
        b -= 1
    
    # Adjust the string to have exactly x transitions
    result = []
    for i in range(len(s)):
        result.append(s[i])
        if i < len(s) - 1 and s[i] != s[i + 1]:
            transition -= 1
        if transition < 0:
            break
    
    # If we have more transitions than needed, we can adjust the last part
    while transition < 0 and len(result) > 1:
        if result[-1] == '0':
            result[-1] = '1'
        else:
            result[-1] = '0'
        transition += 1
    
    print(''.join(result))

# Read input values
a, b, x = map(int, input().split())
construct_binary_string(a, b, x)