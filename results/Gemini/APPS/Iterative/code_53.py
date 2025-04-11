def solve():
    n = int(input())
    a = list(map(int, input().split()))

    l, r = 0, n - 1
    last = -1
    moves = ""
    count = 0

    while l <= r:
        if a[l] > last and a[r] > last:
            if a[l] < a[r]:
                last = a[l]
                moves += "L"
                l += 1
                count += 1
            elif a[r] < a[l]:
                last = a[r]
                moves += "R"
                r -= 1
                count += 1
            else:
                temp_l, temp_r = l, r
                count_l, count_r = 0, 0
                last_l, last_r = last, last
                moves_l, moves_r = "", ""
                
                while temp_l <= r and a[temp_l] > last_l:
                    last_l = a[temp_l]
                    count_l += 1
                    moves_l += "L"
                    temp_l += 1
                
                while temp_r >= l and a[temp_r] > last_r:
                    last_r = a[temp_r]
                    count_r += 1
                    moves_r += "R"
                    temp_r -= 1
                
                if count_l > count_r:
                    moves += moves_l
                    count += count_l
                elif count_r > count_l:
                    moves += moves_r
                    count += count_r
                else:
                    moves += moves_l
                    count += count_l
                break
        elif a[l] > last:
            last = a[l]
            moves += "L"
            l += 1
            count += 1
        elif a[r] > last:
            last = a[r]
            moves += "R"
            r -= 1
            count += 1
        else:
            break
    
    print(count)
    print(moves)

solve()