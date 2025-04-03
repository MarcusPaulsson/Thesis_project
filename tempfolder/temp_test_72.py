def is_beautiful_possible(n, k, a):
    # Create a set of unique elements in the array
    unique_elements = set(a)
    
    # Check if the number of unique elements is greater than k
    if len(unique_elements) > k:
        return False
    
    return True

def create_beautiful_array(n, k, a):
    unique_elements = list(set(a))
    unique_elements.sort()
    
    # Create a beautiful array using the unique elements
    beautiful_array = []
    
    for i in range(10000 // k):  # We want the length to be at most 10^4
        beautiful_array.extend(unique_elements)
    
    return beautiful_array[:10000]  # Ensure the length does not exceed 10^4

def process_test_cases(test_cases):
    results = []
    
    for n, k, a in test_cases:
        if not is_beautiful_possible(n, k, a):
            results.append("-1")
        else:
            beautiful_array = create_beautiful_array(n, k, a)
            results.append(f"{len(beautiful_array)}")
            results.append(" ".join(map(str, beautiful_array)))
    
    return "\n".join(results)

# Read input
t = int(input())
test_cases = []

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    test_cases.append((n, k, a))

# Process test cases and print results
output = process_test_cases(test_cases)
print(output)