def solve():
    n = input()
    s = list(n)
    ans = float('inf')

    for suffix in ["00", "25", "50", "75"]:
        temp_s = s[:]
        moves = 0

        # Find the last digit of the suffix
        idx2 = -1
        for i in range(len(temp_s) - 1, -1, -1):
            if temp_s[i] == suffix[1]:
                idx2 = i
                break
        if idx2 == -1:
            continue

        moves += len(temp_s) - 1 - idx2
        temp_s.pop(idx2)

        # Find the first digit of the suffix
        idx1 = -1
        for i in range(len(temp_s) - 1, -1, -1):
            if temp_s[i] == suffix[0]:
                idx1 = i
                break
        if idx1 == -1:
            continue

        moves += len(temp_s) - 1 - idx1
        temp_s.pop(idx1)

        # Remove leading zeros
        leading_zeros = 0
        for i in range(len(temp_s)):
            if temp_s[i] == '0':
                leading_zeros += 1
            else:
                break

        # Check if all digits are zero after removing suffix
        if leading_zeros == len(temp_s):
            continue
        
        moves += leading_zeros

        ans = min(ans, moves)

    if ans == float('inf'):
        print("-1")
    else:
        print(ans)

solve()