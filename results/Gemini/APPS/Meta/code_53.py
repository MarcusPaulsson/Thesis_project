def solve():
    n = int(input())
    a = list(map(int, input().split()))

    def find_longest_increasing_sequence(arr):
        max_len = 0
        best_moves = ""

        def backtrack(current_sequence, remaining_arr, moves):
            nonlocal max_len, best_moves

            if len(current_sequence) > max_len:
                max_len = len(current_sequence)
                best_moves = moves

            if not remaining_arr:
                return

            last_val = current_sequence[-1] if current_sequence else -1

            # Try taking the leftmost element
            if remaining_arr[0] > last_val:
                backtrack(current_sequence + [remaining_arr[0]], remaining_arr[1:], moves + "L")

            # Try taking the rightmost element
            if len(remaining_arr) > 1 and remaining_arr[-1] > last_val and remaining_arr[0] != remaining_arr[-1]:
                backtrack(current_sequence + [remaining_arr[-1]], remaining_arr[:-1], moves + "R")
            elif len(remaining_arr) == 1 and remaining_arr[-1] > last_val:
                backtrack(current_sequence + [remaining_arr[-1]], remaining_arr[:-1], moves + "R")

        backtrack([], a, "")
        return max_len, best_moves

    length, moves = find_longest_increasing_sequence(a)
    print(length)
    print(moves)

solve()