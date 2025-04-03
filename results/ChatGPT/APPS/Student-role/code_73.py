def mex(arr):
    present = [False] * (len(arr) + 1)
    for num in arr:
        if num < len(present):
            present[num] = True
    for i in range(len(present)):
        if not present[i]:
            return i

def solve():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    t = int(data[0])
    index = 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        a = list(map(int, data[index + 1].split()))
        index += 2
        
        operations = []
        
        for _ in range(2 * n):
            current_mex = mex(a)
            if all(a[i] <= a[i + 1] for i in range(len(a) - 1)):
                break
            
            # Replace the first element that is not in the range [0, n)
            for i in range(n):
                if a[i] >= n or a[i] < 0:
                    a[i] = current_mex
                    operations.append(i + 1)
                    break
            
        results.append(f"{len(operations)}")
        results.append(" ".join(map(str, operations)))
    
    print("\n".join(results))

# Uncomment the following line to run the function directly when needed.
# solve()