def color_array(n, k, a):
    from collections import defaultdict

    # Dictionary to keep track of the frequency of each number
    freq = defaultdict(int)
    for num in a:
        freq[num] += 1

    # If we have any number that appears more than k times, it's impossible
    if any(count > k for count in freq.values()):
        print("NO")
        return

    # Prepare to store the result colors
    result = [0] * n
    color_assignments = defaultdict(list)

    # Assign colors while maintaining the frequency
    for i in range(n):
        num = a[i]
        # Find the next color for this number
        color = len(color_assignments[num]) % k + 1
        color_assignments[num].append(color)
        result[i] = color

    # Check if we have at least one of each color
    if len(set(result)) < k:
        print("NO")
    else:
        print("YES")
        print(' '.join(map(str, result)))

# Input reading
n, k = map(int, input().split())
a = list(map(int, input().split()))
color_array(n, k, a)