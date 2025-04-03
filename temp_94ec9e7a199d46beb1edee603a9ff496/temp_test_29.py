def solve():
    n = int(input())
    a = list(map(int, input().split()))

    def calculate_k_amazing_number(arr, k):
        candidates = set()
        for i in range(n - k + 1):
            subsegment = arr[i:i+k]
            if i == 0:
                candidates = set(subsegment)
            else:
                candidates = candidates.intersection(set(subsegment))
        
        if not candidates:
            return -1
        else:
            return min(candidates)
    
    result = []
    for k in range(1, n + 1):
        result.append(calculate_k_amazing_number(a, k))
    
    print(*result)

t = int(input())
for _ in range(t):
    solve()