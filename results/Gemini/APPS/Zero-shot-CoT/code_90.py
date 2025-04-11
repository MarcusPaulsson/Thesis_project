def solve():
    n, m, d = map(int, input().split())
    c = list(map(int, input().split()))
    
    total_length = sum(c)
    
    if d >= n + 1:
        arr = [0] * n
        arr[n - c[0]:] = [1] * c[0]
        print("YES")
        print(*arr)
        return
    
    arr = [0] * n
    
    pos = 0
    for i in range(m):
        arr[pos:pos + c[i]] = [i + 1] * c[i]
        pos += c[i]
    
    
    def check_reachable(arrangement):
        curr = 0
        while curr < n + 1:
            
            possible_next = []
            for j in range(1, d + 1):
                if curr + j <= n:
                    possible_next.append(curr + j)
                elif curr + j == n + 1:
                    return True
                
            
            next_pos = -1
            for p in possible_next:
                if p <= n and arrangement[p-1] != 0:
                    next_pos = p
                    break
            
            if next_pos == -1:
                return False
            curr = next_pos
        return False

    
    def find_arrangement():
        unused_space = n - sum(c)
        arrangement = [0] * n

        start_positions = []
        curr_pos = 0
        for i in range(m):
            start_positions.append(curr_pos)
            curr_pos += c[i]

        
        def backtrack(k, curr_arrangement):
            if k == m:
                if check_reachable(curr_arrangement):
                    return curr_arrangement
                else:
                    return None
            
            max_start = n - sum(c[k:])
            for start in range(0, unused_space + 1):
                new_arrangement = curr_arrangement[:]
                
                curr_index = 0
                for i in range(k):
                    while curr_index < len(new_arrangement) and new_arrangement[curr_index] != 0:
                        curr_index += 1

                
                platform_start = 0
                if k == 0:
                  platform_start = start
                else:
                  platform_start = sum(c[:k]) + start
                
                
                for i in range(c[k]):
                    new_arrangement[platform_start + i] = k + 1

                
                result = backtrack(k + 1, new_arrangement)
                if result != None:
                    return result
            
            return None

        initial_arrangement = [0] * n
        final_arrangement = backtrack(0, initial_arrangement)

        return final_arrangement
    
    final_arr = find_arrangement()
    
    if final_arr:
        print("YES")
        print(*final_arr)
    else:
        print("NO")

solve()