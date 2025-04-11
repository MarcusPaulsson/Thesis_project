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

            last_val = current_sequence[-1] if current_sequence else 0  # Initialize to 0 for empty sequence

            if remaining_arr[0] > last_val:
                backtrack(current_sequence + [remaining_arr[0]], remaining_arr[1:], moves + "L")

            if len(remaining_arr) > 1 and remaining_arr[-1] > last_val:
                backtrack(current_sequence + [remaining_arr[-1]], remaining_arr[:-1], moves + "R")

        backtrack([], arr, "")
        return max_len, best_moves

    length, moves = find_longest_increasing_sequence(a)
    print(length)
    print(moves)

solve()