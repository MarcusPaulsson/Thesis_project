def nearest_zero(arr):
    n = len(arr)
    distances = [float('inf')] * n
    last_zero = float('-inf')
    for i in range(n):
        if arr[i] == 0:
            last_zero = i
        if last_zero != float('-inf'):
            distances[i] = i - last_zero
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