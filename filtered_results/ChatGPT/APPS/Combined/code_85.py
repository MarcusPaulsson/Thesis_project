def find_price(A, B):
    # Loop through potential prices starting from 1
    for price in range(1, 10000):
        tax_8 = int(price * 0.08)  # Calculate and floor the tax for 8%
        tax_10 = int(price * 0.10)  # Calculate and floor the tax for 10%
        
        # Check if the calculated taxes match A and B
        if tax_8 == A and tax_10 == B:
            return price  # Return the first valid price found
    
    return -1  # Return -1 if no valid price is found

# Read input
A, B = map(int, input().split())
# Get the result and print it
print(find_price(A, B))