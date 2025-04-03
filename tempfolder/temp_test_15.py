def max_window_area(t, test_cases):
    results = []
    for a, b, x, y in test_cases:
        # Calculate areas of rectangles avoiding the dead pixel
        area1 = x * b            # Left of the dead pixel
        area2 = (a - x - 1) * b  # Right of the dead pixel
        area3 = a * y            # Above the dead pixel
        area4 = a * (b - y - 1)  # Below the dead pixel
        
        # The maximum area possible
        max_area = max(area1, area2, area3, area4)
        results.append(max_area)
    
    return results

# Read input
t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]

# Get results
results = max_window_area(t, test_cases)

# Print results
for result in results:
    print(result)