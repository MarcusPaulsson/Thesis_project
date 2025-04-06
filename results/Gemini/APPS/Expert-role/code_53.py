def solve():
    n = int(input())
    a = list(map(int, input().split()))

    def find_longest_increasing_subsequence(arr):
        max_len = 0
        best_moves = ""

        def backtrack(current_sequence, moves, left, right, last_val):
            nonlocal max_len, best_moves
            
            if left > right:
                if len(current_sequence) > max_len:
                    max_len = len(current_sequence)
                    best_moves = moves
                return

            if arr[left] > last_val and arr[right] > last_val:
                if arr[left] < arr[right]:
                    backtrack(current_sequence + [arr[left]], moves + "L", left + 1, right, arr[left])
                    backtrack(current_sequence + [arr[right]], moves + "R", left, right - 1, arr[right])
                elif arr[left] > arr[right]:
                    backtrack(current_sequence + [arr[right]], moves + "R", left, right - 1, arr[right])
                    backtrack(current_sequence + [arr[left]], moves + "L", left + 1, right, arr[left])
                else:
                     backtrack(current_sequence + [arr[left]], moves + "L", left + 1, right, arr[left])
                     backtrack(current_sequence + [arr[right]], moves + "R", left, right - 1, arr[right])
            elif arr[left] > last_val:
                backtrack(current_sequence + [arr[left]], moves + "L", left + 1, right, arr[left])
            elif arr[right] > last_val:
                backtrack(current_sequence + [arr[right]], moves + "R", left, right - 1, arr[right])
            else:
                if len(current_sequence) > max_len:
                    max_len = len(current_sequence)
                    best_moves = moves
                return

        backtrack([], "", 0, n - 1, 0)
        return max_len, best_moves

    length, moves = find_longest_increasing_subsequence(a)
    print(length)
    print(moves)

solve()