def has_cycle(arr):
    n = len(arr)
    if n < 2:
        return False

    visited = [False] * n
    stack = [False] * n

    def is_cyclic(v):
        visited[v] = True
        stack[v] = True

        for i in range(n):
            if arr[i] < arr[v] and not visited[i]:
                if is_cyclic(i):
                    return True
            elif arr[i] < arr[v] and stack[i]:
                return True

        stack[v] = False
        return False

    for i in range(n):
        if not visited[i]:
            if is_cyclic(i):
                return True

    return False

# Driver code
arr = [3, 2, 1, 4]  # Example array
print(has_cycle(arr))