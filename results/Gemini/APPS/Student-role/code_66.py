def solve():
    n, k = map(int, input().split())
    t = input()
    
    def count_occurrences(s, t):
        count = 0
        for i in range(len(s) - len(t) + 1):
            if s[i:i+len(t)] == t:
                count += 1
        return count
    
    best_s = ""
    min_len = float('inf')
    
    for overlap in range(n):
        s = t
        for _ in range(k - 1):
            if overlap > 0:
                if t[overlap:] == t[:n-overlap]:
                    s += t[n-overlap:]
                else:
                    s += t
            else:
                s += t
        
        if count_occurrences(s, t) == k:
            if len(s) < min_len:
                min_len = len(s)
                best_s = s
    print(best_s)

solve()