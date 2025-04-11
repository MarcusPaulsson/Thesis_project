def solve():
    n = input()
    s = list(n)
    l = len(s)
    ans = float('inf')

    for suffix in ['00', '25', '50', '75']:
        temp_s = s[:]
        moves = 0

        # Find the last digit of the suffix
        try:
            idx2 = -1
            for i in range(l - 1, -1, -1):
                if temp_s[i] == suffix[1]:
                    idx2 = i
                    break
            if idx2 == -1:
                continue

            moves += (l - 1 - idx2)
            temp_s.pop(idx2)
        except:
            continue

        # Find the second to last digit of the suffix
        try:
            idx1 = -1
            for i in range(l - 2, -1, -1):
                if temp_s[i] == suffix[0]:
                    idx1 = i
                    break
            if idx1 == -1:
                continue
            
            moves += (l - 2 - idx1)
            temp_s.pop(idx1)
        except:
            continue
        
        # Remove leading zeros
        first_non_zero = -1
        for i in range(len(temp_s)):
            if temp_s[i] != '0':
                first_non_zero = i
                break
        
        if first_non_zero != -1:
            moves += first_non_zero
        
        ans = min(ans, moves)

    if ans == float('inf'):
        print(-1)
    else:
        print(ans)

solve()