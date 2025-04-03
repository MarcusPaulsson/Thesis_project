def solve():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    def calculate_max_strength(arr):
        if not arr:
            return 0
        
        max_strength = 0
        for i in range(1 << len(arr)):
            subsequence = []
            for j in range(len(arr)):
                if (i >> j) & 1:
                    subsequence.append(arr[j])
            
            if not subsequence:
                continue
            
            strength = 0
            for k in range(len(subsequence)):
                if (k % 2 == 0):
                    strength += subsequence[k]
                else:
                    strength -= subsequence[k]
            
            max_strength = max(max_strength, strength)
        return max_strength

    print(calculate_max_strength(a))
    
t = int(input())
for _ in range(t):
    solve()