def solve():
    n = int(input())
    a = list(map(int, input().split()))

    def find_longest_increasing_sequence(arr):
        best_len = 0
        best_moves = ""

        def backtrack(current_sequence, moves, left, right, last_taken):
            nonlocal best_len, best_moves

            if left > right:
                if len(current_sequence) > best_len:
                    best_len = len(current_sequence)
                    best_moves = moves
                return

            if a[left] > last_taken and a[right] > last_taken:
                if a[left] < a[right]:
                    backtrack(current_sequence + [a[left]], moves + "L", left + 1, right, a[left])
                    backtrack(current_sequence + [a[right]], moves + "R", left, right - 1, a[right])
                elif a[left] > a[right]:
                    backtrack(current_sequence + [a[right]], moves + "R", left, right - 1, a[right])
                    backtrack(current_sequence + [a[left]], moves + "L", left + 1, right, a[left])
                else:
                    
                    temp_len_l = 1
                    temp_moves_l = ""
                    
                    curr = a[left]
                    temp_l = left + 1
                    while temp_l <= right and a[temp_l] > curr:
                        curr = a[temp_l]
                        temp_len_l += 1
                        temp_l += 1
                            
                    temp_len_r = 1
                    temp_moves_r = ""
                            
                    curr = a[right]
                    temp_r = right - 1
                    while temp_r >= left and a[temp_r] > curr:
                        curr = a[temp_r]
                        temp_len_r += 1
                        temp_r -= 1
                            
                    if temp_len_l >= temp_len_r:
                        backtrack(current_sequence + [a[left]], moves + "L", left + 1, right, a[left])
                    else:
                        backtrack(current_sequence + [a[right]], moves + "R", left, right - 1, a[right])

            elif a[left] > last_taken:
                backtrack(current_sequence + [a[left]], moves + "L", left + 1, right, a[left])
            elif a[right] > last_taken:
                backtrack(current_sequence + [a[right]], moves + "R", left, right - 1, a[right])
            else:
                if len(current_sequence) > best_len:
                    best_len = len(current_sequence)
                    best_moves = moves
                return

        backtrack([], "", 0, len(arr) - 1, 0)
        return best_len, best_moves

    length, moves = find_longest_increasing_sequence(a)
    print(length)
    print(moves)

solve()