def solve():
    n = input()
    s = list(n)
    n = len(s)

    def calculate_moves(arr, target):
        moves = 0
        temp_arr = arr[:]
        
        # Move the last two digits to the end
        first_target_index = -1
        for i in range(len(temp_arr) - 1, -1, -1):
            if temp_arr[i] == target[1]:
                first_target_index = i
                break
        
        if first_target_index == -1:
            return float('inf')
        
        moves += len(temp_arr) - 1 - first_target_index
        temp_arr.pop(first_target_index)
        
        second_target_index = -1
        for i in range(len(temp_arr) - 1, -1, -1):
            if temp_arr[i] == target[0]:
                second_target_index = i
                break
        
        if second_target_index == -1:
            return float('inf')
        
        moves += len(temp_arr) - 1 - second_target_index
        temp_arr.pop(second_target_index)
        
        # Remove leading zeros
        first_digit_index = -1
        for i in range(len(temp_arr)):
            if temp_arr[i] != '0':
                first_digit_index = i
                break
        
        if first_digit_index == -1:
            return moves
        
        moves += first_digit_index
        
        return moves

    ans = float('inf')
    
    ans = min(ans, calculate_moves(s, "00"))
    ans = min(ans, calculate_moves(s, "25"))
    ans = min(ans, calculate_moves(s, "50"))
    ans = min(ans, calculate_moves(s, "75"))
                
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)

solve()