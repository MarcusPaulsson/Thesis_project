def solve():
    n = int(input())
    a = list(map(int, input().split()))

    unique_vals = sorted(list(set(a)))
    
    def check_sorted(arr):
        for i in range(1, len(arr)):
            if arr[i] < arr[i-1]:
                return False
        return True
    
    if check_sorted(a):
        print(0)
        return

    def get_moves(arr):
        moves = []
        for val in unique_vals:
            moves.append((val, "start"))
            moves.append((val, "end"))
        return moves

    def apply_move(arr, val, direction):
        new_arr = []
        moved_elements = []
        remaining_elements = []
        
        for x in arr:
            if x == val:
                moved_elements.append(x)
            else:
                remaining_elements.append(x)
        
        if direction == "start":
            new_arr = moved_elements + remaining_elements
        else:
            new_arr = remaining_elements + moved_elements
        
        return new_arr
    
    
    min_ops = float('inf')

    
    q = [(a, 0, [])] 
    visited = {tuple(a)}

    while q:
        curr_arr, ops, applied_moves = q.pop(0)

        if check_sorted(curr_arr):
            min_ops = min(min_ops, ops)
            continue
            
        if ops >= min_ops:
            continue

        if ops > len(unique_vals):
            continue
            
        moves = get_moves(curr_arr)

        for val, direction in moves:
            new_arr = apply_move(curr_arr, val, direction)
            
            if tuple(new_arr) not in visited:
                visited.add(tuple(new_arr))
                q.append((new_arr, ops + 1, applied_moves + [(val, direction)]))

    print(min_ops)

q = int(input())
for _ in range(q):
    solve()