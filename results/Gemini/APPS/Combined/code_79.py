def solve():
    n = input()
    s = list(n)
    l = len(s)
    ans = float('inf')

    for suffix in ['00', '25', '50', '75']:
        temp_s = s[:]
        moves = 0

        # Find the last digit of the suffix
        last_digit_index = -1
        for i in range(l - 1, -1, -1):
            if temp_s[i] == suffix[1]:
                last_digit_index = i
                break

        if last_digit_index == -1:
            continue

        moves += l - 1 - last_digit_index
        temp_s.pop(last_digit_index)

        # Find the first digit of the suffix
        first_digit_index = -1
        for i in range(len(temp_s) - 1, -1, -1):
            if temp_s[i] == suffix[0]:
                first_digit_index = i
                break

        if first_digit_index == -1:
            continue

        moves += len(temp_s) - 1 - first_digit_index
        temp_s.pop(first_digit_index)

        # Remove leading zeros
        leading_zeros = 0
        for i in range(len(temp_s)):
            if temp_s[i] == '0':
                leading_zeros += 1
            else:
                break

        # If all digits are zero after removing suffix, it's invalid
        if leading_zeros == len(temp_s):
            continue

        moves += leading_zeros

        ans = min(ans, moves)

    if ans == float('inf'):
        print(-1)
    else:
        print(ans)

solve()