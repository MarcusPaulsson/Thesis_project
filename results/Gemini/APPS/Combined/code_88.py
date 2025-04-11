def solve():
    n = int(input())
    a = list(map(int, input().split()))

    counts = {}
    for x in a:
        counts[x] = counts.get(x, 0) + 1

    matrix = [[0] * n for _ in range(n)]

    def can_place(row, col, num):
        r_sym = n - 1 - row
        c_sym = n - 1 - col

        if row == r_sym and col == c_sym:
            return counts[num] >= 1
        elif row == r_sym or col == c_sym:
            return counts[num] >= 2
        else:
            return counts[num] >= 4

    def place(row, col, num):
        r_sym = n - 1 - row
        c_sym = n - 1 - col

        matrix[row][col] = num
        if row != r_sym or col != c_sym:
            matrix[r_sym][col] = num
        if row != r_sym or col != c_sym:
            matrix[row][c_sym] = num
        if row != r_sym and col != c_sym:
            matrix[r_sym][c_sym] = num

        if row == r_sym and col == c_sym:
            counts[num] -= 1
        elif row == r_sym or col == c_sym:
            counts[num] -= 2
        else:
            counts[num] -= 4

    def remove(row, col, num):
        r_sym = n - 1 - row
        c_sym = n - 1 - col

        matrix[row][col] = 0
        if row != r_sym or col != c_sym:
            matrix[r_sym][col] = 0
        if row != r_sym or col != c_sym:
            matrix[row][c_sym] = 0
        if row != r_sym and col != c_sym:
            matrix[r_sym][c_sym] = 0

        if row == r_sym and col == c_sym:
            counts[num] += 1
        elif row == r_sym or col == c_sym:
            counts[num] += 2
        else:
            counts[num] += 4

    def backtrack(row, col):
        if row == n:
            return True

        if col == n:
            return backtrack(row + 1, 0)

        if matrix[row][col] != 0:
            return backtrack(row, col + 1)

        for num in list(counts.keys()):
            if counts[num] > 0 and can_place(row, col, num):
                place(row, col, num)
                if backtrack(row, col + 1):
                    return True
                remove(row, col, num)

        return False

    if backtrack(0, 0):
        print("YES")
        for row in matrix:
            print(*row)
    else:
        print("NO")

solve()