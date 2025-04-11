def solve():
    n = int(input())
    a = list(map(int, input().split()))

    def find_longest_increasing_subsequence(arr):
        max_len = 0
        best_moves = ""

        def backtrack(current_sequence, left, right, moves):
            nonlocal max_len, best_moves

            if left > right:
                if len(current_sequence) > max_len:
                    max_len = len(current_sequence)
                    best_moves = moves
                return

            if not current_sequence:
                # Take left
                backtrack(current_sequence + [arr[left]], left + 1, right, moves + "L")
                # Take right
                backtrack(current_sequence + [arr[right]], left, right - 1, moves + "R")
            else:
                last_element = current_sequence[-1]
                
                # Take left
                if arr[left] > last_element:
                    backtrack(current_sequence + [arr[left]], left + 1, right, moves + "L")
                
                # Take right
                if arr[right] > last_element:
                    backtrack(current_sequence + [arr[right]], left, right - 1, moves + "R")
                

        backtrack([], 0, len(arr) - 1, "")
        return max_len, best_moves
    
    def find_longest_increasing_subsequence_optimized(arr):
        n = len(arr)
        dp = {}

        def solve_recursive(left, right, last):
            if (left, right, last) in dp:
                return dp[(left, right, last)]

            if left > right:
                return 0, ""

            len_l, len_r = 0, 0
            moves_l, moves_r = "", ""

            if arr[left] > last:
                len_l, moves_l = solve_recursive(left + 1, right, arr[left])
                len_l += 1
                moves_l = "L" + moves_l

            if arr[right] > last:
                len_r, moves_r = solve_recursive(left, right - 1, arr[right])
                len_r += 1
                moves_r = "R" + moves_r
            
            if len_l > len_r:
                dp[(left, right, last)] = len_l, moves_l
            elif len_r > len_l:
                dp[(left, right, last)] = len_r, moves_r
            elif len_l == len_r and len_l != 0:
                dp[(left, right, last)] = len_l, min(moves_l, moves_r)
            else:
                dp[(left, right, last)] = 0, ""
            
            return dp[(left, right, last)]

        length, moves = solve_recursive(0, n - 1, 0)
        return length, moves

    length, moves = find_longest_increasing_subsequence_optimized(a)
    print(length)
    print(moves)

solve()