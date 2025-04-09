def solve():
    n = input()
    s = list(n)
    l = len(s)
    
    def calculate_moves(arr):
        moves = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] > arr[j]:
                    moves += 1
        return moves
    
    def get_moves(a, b):
        temp = s[:]
        moves = 0
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        idx_a = -1
        for i in range(l - 1, -1, -1):
            if temp[i] == a:
                idx_a = i
                break
        if idx_a == -1:
            return float('inf')
        
        moves += l - 1 - idx_a
        temp.pop(idx_a)
        
        idx_b = -1
        for i in range(len(temp) - 1, -1, -1):
            if temp[i] == b:
                idx_b = i
                break
        if idx_b == -1:
            return float('inf')
        
        moves += len(temp) - 1 - idx_b
        temp.pop(idx_b)
        
        
        first_non_zero = -1
        for i in range(len(temp)):
            if temp[i] != '0':
                first_non_zero = i
                break
        
        if first_non_zero == -1:
            return float('inf')
        
        moves += first_non_zero
        
        return moves
        
    ans = min(get_moves('0', '0'), get_moves('2', '5'), get_moves('5', '0'), get_moves('7', '5'))
    
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)

solve()