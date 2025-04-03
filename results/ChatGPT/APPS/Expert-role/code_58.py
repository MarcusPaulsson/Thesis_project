def color_array(n, k, a):
    from collections import defaultdict

    # Map to keep track of the occurrences of each number
    occurrence = defaultdict(list)

    # Fill the occurrence map
    for index, value in enumerate(a):
        occurrence[value].append(index)

    # Check if we can color the array
    if len(occurrence) > k:
        print("NO")
        return

    # Prepare the result array
    result = [0] * n
    color = 1

    # Assign colors
    for numbers in occurrence.values():
        for i, index in enumerate(numbers):
            result[index] = (i % k) + 1

    print("YES")
    print(' '.join(map(str, result)))

# Example usage with input reading
n, k = map(int, input().split())
a = list(map(int, input().split()))
color_array(n, k, a)