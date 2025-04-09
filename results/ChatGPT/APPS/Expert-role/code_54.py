def min_D_to_equal(a):
    a_min = min(a)
    a_max = max(a)

    if a_min == a_max:
        return 0

    # The distance we need to cover
    distance = a_max - a_min

    # If there are only two distinct elements
    if len(set(a)) == 2:
        return distance // 2

    # If there are more than two distinct elements
    unique_values = sorted(set(a))
    
    if len(unique_values) > 3 or (len(unique_values) == 3 and unique_values[2] - unique_values[0] != unique_values[1] - unique_values[0]):
        return -1
    
    # If we have exactly three unique values
    if len(unique_values) == 3:
        if unique_values[2] - unique_values[1] == unique_values[1] - unique_values[0]:
            return unique_values[1] - unique_values[0]
        else:
            return -1

    return -1

# Input reading
n = int(input())
a = list(map(int, input().split()))

# Output the result
print(min_D_to_equal(a))