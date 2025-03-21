def solve():
    n, k = map(int, input().split())
    s = input()

    def calculate_score(s):
        score = 0
        for i in range(len(s)):
            if s[i] == 'W':
                if i == 0:
                    score += 1
                elif s[i-1] == 'W':
                    score += 2
                else:
                    score += 1
        return score
    
    max_score = 0
    for i in range(1 << n):
        temp_s = list(s)
        changes = 0
        for j in range(n):
            if (i >> j) & 1:
                if temp_s[j] == 'W':
                    temp_s[j] = 'L'
                else:
                    temp_s[j] = 'W'
                changes += 1
        
        if changes <= k:
            max_score = max(max_score, calculate_score("".join(temp_s)))

    
    
    initial_wins = s.count('W')
    if initial_wins + k >= n:
        print(2 * n - 1)
        return

    
    wins = 0
    for i in range(n):
        if s[i] == 'W':
            wins += 1
    
    if wins == 0:
        if k == 0:
            print(0)
        else:
            print(2 * k - 1)
        return
    

    gaps = []
    start = -1
    end = -1
    
    first_win = -1
    last_win = -1
    
    for i in range(n):
        if s[i] == 'W':
            if first_win == -1:
                first_win = i
            last_win = i
    
    i = 0
    while i < n:
        if s[i] == 'L':
            start = i
            while i < n and s[i] == 'L':
                i += 1
            end = i - 1
            gaps.append((start, end))
        else:
            i += 1
    
    gaps.sort(key=lambda x: x[1] - x[0] + 1)
    
    new_s = list(s)
    
    for start, end in gaps:
        length = end - start + 1
        if k >= length:
            for i in range(start, end + 1):
                new_s[i] = 'W'
            k -= length
    
    
    
    if k > 0:
        for i in range(n):
            if new_s[i] == 'L' and k > 0:
                new_s[i] = 'W'
                k -= 1
    
    

    print(calculate_score("".join(new_s)))

t = int(input())
for _ in range(t):
    solve()