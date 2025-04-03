def mex(arr):
    present = [False] * (len(arr) + 1)
    for num in arr:
        if num <= len(arr):
            present[num] = True
    for i in range(len(arr) + 1):
        if not present[i]:
            return i

def solve_case(n, a):
    operations = []
    
    # Check if already non-decreasing
    if all(a[i] <= a[i + 1] for i in range(n - 1)):
        return 0, []
    
    for _ in range(2 * n):
        current_mex = mex(a)
        for i in range(n):
            if a[i] > current_mex:
                operations.append(i + 1)  # Store 1-based index
                a[i] = current_mex
                break
        
        if all(a[i] <= a[i + 1] for i in range(n - 1)):
            break
    
    return len(operations), operations

t = int(input())
results = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    k, ops = solve_case(n, a)
    results.append((k, ops))

for k, ops in results:
    print(k)
    if ops:
        print(" ".join(map(str, ops)))
    else:
        print()