def solve():
    n, s = input().split()
    n = int(n)
    
    def get_min_lis(n, s):
        perm = [0] * n
        nums = list(range(1, n + 1))
        
        idx = 0
        i = 0
        while i < n:
            j = i
            while j < n - 1 and s[j] == '>':
                j += 1
            
            for k in range(j, i - 1, -1):
                perm[k] = nums[idx]
                idx += 1
            i = j + 1
        return perm
    
    def get_max_lis(n, s):
        perm = [0] * n
        nums = list(range(1, n + 1))
        
        idx = 0
        i = 0
        while i < n:
            j = i
            while j < n - 1 and s[j] == '<':
                j += 1
                
            for k in range(j, i - 1, -1):
                perm[k] = nums[idx]
                idx += 1
            i = j + 1
        return perm
        
    print(*get_min_lis(n, s))
    print(*get_max_lis(n, s))

t = int(input())
for _ in range(t):
    solve()