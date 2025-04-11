def solve():
    n, k = map(int, input().split())

    if k == 1:
        print("YES")
        print(n)
        return

    
    def check(first):
        arr = [first]
        total = first
        for _ in range(k - 1):
            next_val = arr[-1] + 1
            if next_val > 2 * arr[-1]:
                return False, []
            arr.append(next_val)
            total += next_val
        
        if total > n:
            return False, []
        
        diff = n - total
        
        for i in range(k - 1, -1, -1):
            add = min(diff, 2 * arr[i] - arr[i] - (arr[i] - (arr[i-1] if i > 0 else 0) if i > 0 else 0))
            arr[i] += add
            diff -= add
            
            if diff == 0:
                break
        
        if diff > 0:
            return False, []
        
        
        for i in range(k - 1):
            if not (arr[i] < arr[i+1] <= 2 * arr[i]):
                return False, []
        
        return True, arr

    for first in range(1, n + 1):
        possible, arr = check(first)
        if possible:
            print("YES")
            print(*arr)
            return

    print("NO")

solve()