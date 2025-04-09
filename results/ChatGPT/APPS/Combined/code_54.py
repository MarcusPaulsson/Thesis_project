def minimum_d(n, a):
    min_a = min(a)
    max_a = max(a)

    # If all elements are equal, return 0
    if min_a == max_a:
        return 0

    # Calculate the difference
    diff = max_a - min_a

    # If the difference is odd, it's impossible to make all elements equal
    if diff % 2 != 0:
        return -1

    # Return the minimum D
    return diff // 2

# Read input
n = int(input().strip())
a = list(map(int, input().strip().split()))

# Print the result
print(minimum_d(n, a))