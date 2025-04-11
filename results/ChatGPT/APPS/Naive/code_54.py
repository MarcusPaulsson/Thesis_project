def minimum_D(n, a):
    min_a = min(a)
    max_a = max(a)

    if min_a == max_a:
        return 0  # All elements are already equal

    # The potential target value to make all elements equal
    target1 = min_a + (max_a - min_a) // 2
    target2 = max_a - (max_a - min_a) // 2

    # Calculate the required D for both targets
    D1 = max(0, target1 - min_a, max_a - target1)
    D2 = max(0, target2 - min_a, max_a - target2)

    # Check if we can achieve target1 or target2
    def can_achieve(target):
        return all(abs(x - target) <= D1 for x in a)

    if can_achieve(target1):
        return D1
    elif can_achieve(target2):
        return D2
    else:
        return -1

# Input reading
n = int(input())
a = list(map(int, input().split()))

# Output the result
print(minimum_D(n, a))