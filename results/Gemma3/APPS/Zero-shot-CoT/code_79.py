def solve():
    n = input()
    n_len = len(n)
    
    def is_divisible_by_25(num_str):
        if len(num_str) >= 2:
            last_two_digits = int(num_str[-2:])
            return last_two_digits % 25 == 0
        else:
            return False
    
    q = [(n, 0)]
    visited = {n}
    
    while q:
        curr_num, moves = q.pop(0)
        
        if is_divisible_by_25(curr_num):
            print(moves)
            return
        
        for i in range(n_len - 1):
            next_num = list(curr_num)
            next_num[i], next_num[i+1] = next_num[i+1], next_num[i]
            next_num = "".join(next_num)
            
            if next_num[0] == '0' and len(next_num) > 1:
                continue
            
            if next_num not in visited:
                visited.add(next_num)
                q.append((next_num, moves + 1))
    
    print(-1)

solve()