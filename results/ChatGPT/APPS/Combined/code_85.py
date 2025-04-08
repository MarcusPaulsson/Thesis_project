def find_price(A, B):
    for price in range(1, 10001):  # Increased upper limit for better coverage
        if (price * 0.08 // 1 == A) and (price * 0.10 // 1 == B):
            return price
    return -1

# Read input
A, B = map(int, input().strip().split())
# Find and print the result
print(find_price(A, B))