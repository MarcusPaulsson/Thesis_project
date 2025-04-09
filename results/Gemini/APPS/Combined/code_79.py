def solve():
    n = input()
    n_list = list(n)
    length = len(n)

    def calculate_moves(arr, target):
        moves = 0
        arr_copy = arr[:]

        # Find the last digit
        last_index = -1
        for i in range(length - 1, -1, -1):
            if arr_copy[i] == target[1]:
                last_index = i
                break

        if last_index == -1:
            return float('inf')

        moves += (length - 1) - last_index
        arr_copy.pop(last_index)

        # Find the second last digit
        second_last_index = -1
        for i in range(len(arr_copy) - 1, -1, -1):
            if arr_copy[i] == target[0]:
                second_last_index = i
                break

        if second_last_index == -1:
            return float('inf')

        moves += (len(arr_copy) - 1) - second_last_index
        arr_copy.pop(second_last_index)

        # Remove leading zeros
        leading_zeros = 0
        for i in range(len(arr_copy)):
            if arr_copy[i] == '0':
                leading_zeros += 1
            else:
                break

        moves += leading_zeros
        if len(arr_copy) > 0 and arr_copy[0] == '0':
            return float('inf')
        
        return moves

    min_moves = float('inf')

    targets = ['00', '25', '50', '75']

    for target in targets:
        min_moves = min(min_moves, calculate_moves(n_list[:], target))

    if min_moves == float('inf'):
        print("-1")
    else:
        print(min_moves)

solve()