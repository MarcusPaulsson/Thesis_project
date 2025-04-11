def nearest_zero(arr):
    """
    Calculates the distance to the nearest zero for each element in the array.

    Args:
        arr (list): A list of integers.

    Returns:
        list: A list of integers representing the distances to the nearest zero.
    """

    n = len(arr)
    distances = [float('inf')] * n

    # Forward pass: Calculate distances from left to right
    last_zero = float('-inf')
    for i in range(n):
        if arr[i] == 0:
            last_zero = i
        if last_zero != float('-inf'):
            distances[i] = min(distances[i], i - last_zero)

    # Backward pass: Calculate distances from right to left
    last_zero = float('inf')
    for i in range(n - 1, -1, -1):
        if arr[i] == 0:
            last_zero = i
        if last_zero != float('inf'):
            distances[i] = min(distances[i], last_zero - i)

    return distances


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    result = nearest_zero(arr)
    print(*result)