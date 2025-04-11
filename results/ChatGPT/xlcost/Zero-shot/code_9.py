def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def distinct_elements(arr):
    distinct_set = set(arr)
    while True:
        new_elements = set()
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                new_elements.add(abs(arr[i] - arr[j]))
        new_elements.difference_update(distinct_set)
        if not new_elements:
            break
        distinct_set.update(new_elements)
    return distinct_set

def count_non(arr):
    max_value = max(arr)
    gcd_value = arr[0]
    for num in arr:
        gcd_value = gcd(gcd_value, num)
    
    distinct_set = distinct_elements(arr)
    
    return len(distinct_set), max_value, gcd_value

# Example usage:
# arr = [your_array_here]
# result = count_non(arr)
# print(result)