def solve():
    n = input()
    n_list = list(n)
    length = len(n)
    
    def calculate_moves(arr, a, b):
        moves = 0
        
        # Move b to the end
        b_index = -1
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] == b:
                b_index = i
                break
        
        if b_index == -1:
            return float('inf')
            
        for i in range(b_index, len(arr) - 1):
            arr[i], arr[i+1] = arr[i+1], arr[i]
            moves += 1
            
        # Move a to the second to last position
        a_index = -1
        for i in range(len(arr) - 2, -1, -1):
            if arr[i] == a:
                a_index = i
                break
                
        if a_index == -1:
            return float('inf')
        
        for i in range(a_index, len(arr) - 2):
            arr[i], arr[i+1] = arr[i+1], arr[i]
            moves += 1
            
        # Remove leading zeros
        first_non_zero = -1
        for i in range(len(arr)):
            if arr[i] != '0':
                first_non_zero = i
                break
        
        if first_non_zero == -1:
            return float('inf')

        moves += first_non_zero
        
        return moves
    
    min_moves = float('inf')
    
    min_moves = min(min_moves, calculate_moves(n_list[:], '0', '0'))
    min_moves = min(min_moves, calculate_moves(n_list[:], '2', '5'))
    min_moves = min(min_moves, calculate_moves(n_list[:], '5', '0'))
    min_moves = min(min_moves, calculate_moves(n_list[:], '7', '5'))
    
    if min_moves == float('inf'):
        print("-1")
    else:
        print(min_moves)
        
solve()