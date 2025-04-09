def solve():
    n = int(input())
    a = list(map(int, input().split()))

    counts = {}
    for x in a:
        counts[x] = counts.get(x, 0) + 1

    matrix = [[0] * n for _ in range(n)]

    def can_fill(row, col):
        if row >= n:
            return True

        if col >= n:
            return can_fill(row + 1, 0)

        if matrix[row][col] != 0:
            return can_fill(row, col + 1)

        row_sym = n - 1 - row
        col_sym = n - 1 - col

        candidates = list(counts.keys())
        for num in candidates:
            if counts[num] > 0:
                counts[num] -= 1
                matrix[row][col] = num

                if row == row_sym and col == col_sym:
                    if can_fill(row, col + 1):
                        return True
                elif row == row_sym:
                    if matrix[row][col_sym] == 0:
                        matrix[row][col_sym] = num
                        if can_fill(row, col + 1):
                            return True
                        matrix[row][col_sym] = 0
                    else:
                        if matrix[row][col_sym] == num:
                            if can_fill(row, col + 1):
                                return True
                elif col == col_sym:
                    if matrix[row_sym][col] == 0:
                        matrix[row_sym][col] = num
                        if can_fill(row, col + 1):
                            return True
                        matrix[row_sym][col] = 0
                    else:
                        if matrix[row_sym][col] == num:
                            if can_fill(row, col + 1):
                                return True
                else:
                    if matrix[row_sym][col] == 0 and matrix[row][col_sym] == 0 and matrix[row_sym][col_sym] == 0:
                        matrix[row_sym][col] = num
                        matrix[row][col_sym] = num
                        matrix[row_sym][col_sym] = num
                        if can_fill(row, col + 1):
                            return True
                        matrix[row_sym][col] = 0
                        matrix[row][col_sym] = 0
                        matrix[row_sym][col_sym] = 0
                    elif matrix[row_sym][col] == num and matrix[row][col_sym] == num and matrix[row_sym][col_sym] == num:
                        if can_fill(row, col + 1):
                            return True

                matrix[row][col] = 0
                counts[num] += 1

        return False

    total_elements = n * n
    needed = {1: 0, 2: 0, 4: 0}

    if n % 2 == 1:
        needed[1] = 1
        needed[2] = n // 2 * 2
        needed[4] = (n // 2) * (n // 2)
    else:
        needed[1] = 0
        needed[2] = 0
        needed[4] = (n // 2) * (n // 2)

    counts_needed = {1: 0, 2: 0, 4: 0}
    for count in counts.values():
        if count >= 4:
            counts_needed[4] += count // 4
            count %= 4
        if count >= 2:
            counts_needed[2] += count // 2
            count %= 2
        if count >= 1:
            counts_needed[1] += count

    one_center = n % 2 == 1
    two_mid = n % 2 == 1
    four_quad = True

    if can_fill(0, 0):
        print("YES")
        for row in matrix:
            print(*row)
    else:
        print("NO")

solve()