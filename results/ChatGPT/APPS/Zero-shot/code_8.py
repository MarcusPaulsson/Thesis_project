def color_array(n, k, a):
    from collections import defaultdict

    # Dictionary to hold the indices of each number
    positions = defaultdict(list)
    
    for index, value in enumerate(a):
        positions[value].append(index)

    # If any number appears more than k times, it's impossible
    if any(len(positions[num]) > k for num in positions):
        return "NO"

    # Prepare the result array and color allocation
    result = [0] * n
    color = 1

    # Assign colors to each number's positions
    for num, indices in positions.items():
        for idx in indices:
            result[idx] = color
            color += 1
            if color > k:
                color = 1

    # Check if we have used all colors
    if len(set(result)) < k:
        return "NO"

    return "YES", result

# Input reading
n, k = map(int, input().split())
a = list(map(int, input().split()))

# Get the result
result = color_array(n, k, a)

# Print the output
if result == "NO":
    print(result)
else:
    print(result[0])
    print(' '.join(map(str, result[1])))