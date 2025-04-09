def nearest_zero(arr):
    """
    Calculates the distance to the nearest zero for each element in the array.

    Args:
        arr: A list of integers.

    Returns:
        A list of integers representing the distances to the nearest zero.
    """

    n = len(arr)
    distances = [float('inf')] * n

    # Forward pass: Find the distance to the nearest zero from the left
    last_zero_index = float('-inf')
    for i in range(n):
        if arr[i] == 0:
            last_zero_index = i
            distances[i] = 0
        elif last_zero_index != float('-inf'):
            distances[i] = min(distances[i], i - last_zero_index)

    # Backward pass: Find the distance to the nearest zero from the right
    last_zero_index = float('inf')
    for i in range(n - 1, -1, -1):
        if arr[i] == 0:
            last_zero_index = i
            distances[i] = 0
        elif last_zero_index != float('inf'):
            distances[i] = min(distances[i], last_zero_index - i)

    return distances


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    result = nearest_zero(arr)
    print(*result)