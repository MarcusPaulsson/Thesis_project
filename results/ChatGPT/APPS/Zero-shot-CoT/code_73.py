def mex(arr):
    present = [False] * (len(arr) + 1)
    for num in arr:
        if 0 <= num <= len(arr):
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
        
        while True:
            current_mex = mex(a)
            if all(a[i] <= a[i+1] for i in range(n - 1)):
                break
            
            # Find the first index that we can replace
            for i in range(n):
                if a[i] > current_mex:
                    operations.append(i + 1)  # Store 1-based index
                    a[i] = current_mex
                    break
        
        results.append(f"{len(operations)}")
        results.append(" ".join(map(str, operations)))
    
    print("\n".join(results))

# Uncomment the line below to run the solve function
# solve()