def find_integer_pair(x):
    target_product = round(x * 10)
    
    for a in range(1, 11):
        for b in range(1, 11):
            if a * b == target_product:
                return a, b

# Read input and convert to float
x = float(input().strip())
a, b = find_integer_pair(x)

# Print the result
print(a, b)