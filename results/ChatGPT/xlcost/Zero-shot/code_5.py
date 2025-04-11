from collections import defaultdict

def countQuadruples(arr):
    product_map = defaultdict(int)
    n = len(arr)
    
    # Generate all possible pairs and store their products
    for i in range(n):
        for j in range(i + 1, n):
            product = arr[i] * arr[j]
            product_map[product] += 1
    
    count = 0
    
    # Count the quadruples based on the products
    for prod in product_map:
        if product_map[prod] > 1:
            # If there are k pairs with the same product, we can choose 2 pairs from k
            k = product_map[prod]
            count += (k * (k - 1)) // 2  # Combination of k pairs taken 2 at a time
    
    return count

# Driver code
# Example usage:
# arr = [1, 2, 3, 4]
# result = countQuadruples(arr)
# print(result)