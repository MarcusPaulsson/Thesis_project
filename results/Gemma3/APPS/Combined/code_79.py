from collections import deque

def solve():
    n = input()
    n_len = len(n)
    
    def is_divisible_by_25(num_str):
        if len(num_str) < 2:
            return False
        last_two_digits = int(num_str[-2:])
        return last_two_digits % 25 == 0

    def get_min_moves(num_str):
        q = deque([(num_str, 0)])
        visited = {num_str}
        
        while q:
            curr_num, moves = q.popleft()
            
            if is_divisible_by_25(curr_num):
                return moves
            
            for i in range(len(curr_num) - 1):
                next_num = list(curr_num)
                next_num[i], next_num[i+1] = next_num[i+1], next_num[i]
                next_num = "".join(next_num)
                
                if next_num[0] == '0' and len(next_num) > 1:
                    continue
                
                if next_num not in visited:
                    q.append((next_num, moves + 1))
                    visited.add(next_num)
        
        return -1

    result = get_min_moves(n)
    print(result)

solve()