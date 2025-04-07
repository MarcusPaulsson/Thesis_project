from collections import Counter

def restore_xy(n, divisors):
    count = Counter(divisors)
    
    # Identify the maximum divisor, which is the candidate for x or y
    max_divisor = max(divisors)
    
    # Find the second maximum divisor which must be x or y
    second_max_divisor = 1
    for d in divisors:
        if d < max_divisor:
            second_max_divisor = max(second_max_divisor, d)
    
    # Calculate potential x and y
    x = max_divisor
    y = second_max_divisor
    
    # Ensure y is the correct value by checking divisor counts
    temp_count = count.copy()
    
    for d in divisors:
        if x % d == 0 and temp_count[d] > 0:
            temp_count[d] -= 1
        if y % d == 0 and temp_count[d] > 0:
            temp_count[d] -= 1
    
    # Check if all counts are satisfied
    if all(v == 0 for v in temp_count.values()):
        return x, y
    
    return None

# Input reading
n = int(input())
divisors = list(map(int, input().split()))

# Call the function and print the result
result = restore_xy(n, divisors)
if result:
    print(result[0], result[1])