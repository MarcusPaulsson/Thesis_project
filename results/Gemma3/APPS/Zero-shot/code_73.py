def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    def can_complete(arr):
        if len(arr) == 0:
            return True
        
        target_height = arr[0]
        for height in arr:
            if height != target_height:
                return False
        return True
    
    def possible_moves(arr):
        moves = []
        for i in range(len(arr) - 1):
            if arr[i] == arr[i+1]:
                moves.append(i)
        return moves
    
    def apply_move(arr, move_index):
        new_arr = arr[:]
        new_arr[move_index] += 1
        new_arr[move_index+1] += 1
        return new_arr
    
    q = [a]
    visited = {tuple(a)}
    
    while q:
        curr_arr = q.pop(0)
        
        if can_complete(curr_arr):
            print("YES")
            return
        
        moves = possible_moves(curr_arr)
        
        for move_index in moves:
            next_arr = apply_move(curr_arr, move_index)
            
            if tuple(next_arr) not in visited:
                q.append(next_arr)
                visited.add(tuple(next_arr))
    
    print("NO")

solve()