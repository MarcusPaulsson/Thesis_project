def mex(arr):
    present = [False] * (len(arr) + 1)
    for num in arr:
        if num < len(present):
            present[num] = True
    for i in range(len(present)):
        if not present[i]:
            return i
    return len(present)

def make_non_decreasing(arr):
    n = len(arr)
    operations = []
    
    for _ in range(2 * n):
        current_mex = mex(arr)
        if all(arr[i] <= arr[i + 1] for i in range(n - 1)):  # Check if already non-decreasing
            break
        # Replace any element with the current_mex
        for i in range(n):
            if arr[i] != current_mex:  # We can safely replace
                arr[i] = current_mex
                operations.append(i + 1)  # Store 1-based index
                break

    return operations

t = int(input())
results = []
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    operations = make_non_decreasing(arr)
    
    results.append(f"{len(operations)}")
    if operations:
        results.append(" ".join(map(str, operations)))
    else:
        results.append("")

print("\n".join(results))