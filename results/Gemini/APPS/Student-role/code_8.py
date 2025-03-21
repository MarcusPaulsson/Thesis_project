def solve():
    n, k = map(int, input().split())
    s = input()

    def calculate_score(arr):
        score = 0
        for i in range(len(arr)):
            if arr[i] == 'W':
                if i == 0:
                    score += 1
                elif arr[i-1] == 'W':
                    score += 2
                else:
                    score += 1
        return score

    def find_optimal_score(arr, k_left):
        if k_left == 0:
            return calculate_score(arr)

        max_score = calculate_score(arr)
        
        indices_to_change = []
        for i in range (len(arr)):
            if arr[i] == 'L':
                indices_to_change.append(i)
                
        if len(indices_to_change) == 0:
            return calculate_score(arr)
            
        for i in indices_to_change:
            temp_arr = list(arr)
            temp_arr[i] = 'W'
            
            max_score = max(max_score, find_optimal_score("".join(temp_arr), k_left-1))
                
        return max_score
    
    
    
    
    def solve_dp():
        max_score = 0
        
        for i in range(1 << n):
            num_changes = 0
            temp_s = list(s)
            
            for j in range(n):
                if (i >> j) & 1:
                    if temp_s[j] == 'W':
                        temp_s[j] = 'L'
                    else:
                        temp_s[j] = 'W'
                    num_changes += 1
                    
            if num_changes <= k:
                max_score = max(max_score, calculate_score(temp_s))
        return max_score

    
    
    
    wins = s.count('W')
    if wins == 0:
        if k == 0:
            print(0)
        else:
            print(2 * k - 1) if k <= n else print(2 * n -1)
        return

    
    gaps = []
    first_win = -1
    last_win = -1
    
    for i in range(n):
        if s[i] == 'W':
            if first_win == -1:
                first_win = i
            last_win = i
            
    
    current_gap = 0
    for i in range(first_win + 1, last_win + 1):
        if s[i] == 'L':
            current_gap += 1
        elif current_gap > 0:
            gaps.append(current_gap)
            current_gap = 0
            
    gaps.sort()
    
    score = calculate_score(s)
    
    for gap in gaps:
        if k >= gap:
            score += 2 * gap + 1
            k -= gap
        else:
            score += 2 * k
            k = 0
            break
    
    if k > 0:
        score += 2 * k
        
        if first_win == 0 and last_win == n -1:
            pass
        elif first_win == 0 or last_win == n-1:
            score -= k
        else:
            score -= k
    
    
    print(min(score, 2 * n - 1))
    

t = int(input())
for _ in range(t):
    solve()