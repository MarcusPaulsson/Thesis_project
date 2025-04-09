def find_x_and_y(divisors):
    from collections import Counter
    import math

    # Count occurrences of each divisor
    divisor_count = Counter(divisors)

    # Find the largest divisor, which will be one of the numbers (either x or y)
    max_divisor = max(divisor_count)

    # Calculate the product of all divisors
    product_of_divisors = 1
    for divisor, count in divisor_count.items():
        product_of_divisors *= divisor ** count

    # Calculate the other number using the product
    other_number = product_of_divisors // max_divisor

    return max_divisor, other_number

# Input reading
n = int(input().strip())
divisors = list(map(int, input().strip().split()))

# Finding x and y
x, y = find_x_and_y(divisors)

# Output the result
print(x, y)