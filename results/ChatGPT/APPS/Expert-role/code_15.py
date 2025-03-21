def max_window_area(t, cases):
    results = []
    for a, b, x, y in cases:
        # Calculate areas by excluding the dead pixel
        area_up = (x + 1) * b  # area above the dead pixel
        area_down = (a - x) * b  # area below the dead pixel
        area_left = a * (y + 1)  # area left of the dead pixel
        area_right = a * (b - y)  # area right of the dead pixel
        
        # The maximal area without the dead pixel
        max_area = max(area_up, area_down, area_left, area_right)
        results.append(max_area)
    
    return results

# Input handling
t = int(input())
cases = [tuple(map(int, input().split())) for _ in range(t)]
results = max_window_area(t, cases)

# Output results
for result in results:
    print(result)