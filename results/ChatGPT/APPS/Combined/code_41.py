def nearest_zero_distance(n, arr):
    distances = [float('inf')] * n
    last_zero_index = -1

    # Forward pass to find distances to the nearest zero on the left
    for i in range(n):
        if arr[i] == 0:
            last_zero_index = i
            distances[i] = 0
        elif last_zero_index != -1:
            distances[i] = i - last_zero_index

    # Backward pass to find distances to the nearest zero on the right
    last_zero_index = -1
    for i in range(n - 1, -1, -1):
        if arr[i] == 0:
            last_zero_index = i
        elif last_zero_index != -1:
            distances[i] = min(distances[i], last_zero_index - i)

    print(' '.join(map(str, distances)))

# Example usage
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    nearest_zero_distance(n, arr)