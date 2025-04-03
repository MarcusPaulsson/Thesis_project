def make_beautiful_array(t, test_cases):
    results = []
    for case in test_cases:
        n, k, a = case
        # Initialize frequency array
        freq = [0] * (n + 1)
        
        # Count occurrences of each number in the array
        for num in a:
            freq[num] += 1
        
        # To store the sequence of unique elements for the beautiful array
        unique_elements = []
        
        # Collect unique elements that we can use from 1 to n
        for i in range(1, n + 1):
            if freq[i] > 0:
                unique_elements.append(i)
        
        # Check if we can form a beautiful array
        if len(unique_elements) > k:
            results.append("-1")
            continue
        
        # Create the beautiful array
        m = max(10000, len(unique_elements) * k)
        beautiful_array = []
        
        # Repeat the unique elements to fill up to m
        while len(beautiful_array) < m:
            for element in unique_elements:
                if len(beautiful_array) < m:
                    beautiful_array.append(element)
        
        results.append(f"{len(beautiful_array)}")
        results.append(" ".join(map(str, beautiful_array)))
    
    return results

# Example usage
t = 4
test_cases = [
    (4, 2, [1, 2, 2, 1]),
    (4, 3, [1, 2, 2, 1]),
    (3, 2, [1, 2, 3]),
    (4, 4, [4, 3, 4, 2])
]

output = make_beautiful_array(t, test_cases)
for line in output:
    print(line)