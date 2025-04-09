def solve():
    n = int(input())
    a = list(map(int, input().split()))

    def find_longest_increasing_subsequence(arr):
        l, r = 0, len(arr) - 1
        last = 0
        moves = ""
        result = []

        while l <= r:
            if arr[l] > last and arr[r] > last:
                if arr[l] < arr[r]:
                    result.append(arr[l])
                    moves += "L"
                    last = arr[l]
                    l += 1
                elif arr[r] < arr[l]:
                    result.append(arr[r])
                    moves += "R"
                    last = arr[r]
                    r -= 1
                else:
                    temp_l = ""
                    temp_r = ""
                    last_l = last
                    last_r = last
                    len_l = 0
                    len_r = 0
                    l_temp = l
                    r_temp = r

                    while l_temp <= r and arr[l_temp] > last_l:
                        temp_l += "L"
                        last_l = arr[l_temp]
                        l_temp += 1
                        len_l +=1
                    
                    while l <= r_temp and arr[r_temp] > last_r:
                        temp_r += "R"
                        last_r = arr[r_temp]
                        r_temp -= 1
                        len_r += 1
                    
                    if len_l > len_r:
                        moves += temp_l
                        result.extend(arr[l:l+len_l])
                        return len(result), moves
                    else:
                        moves += temp_r
                        result.extend(arr[r+1-len_r:r+1])
                        return len(result), moves
            elif arr[l] > last:
                result.append(arr[l])
                moves += "L"
                last = arr[l]
                l += 1
            elif arr[r] > last:
                result.append(arr[r])
                moves += "R"
                last = arr[r]
                r -= 1
            else:
                break

        return len(result), moves

    length, moves = find_longest_increasing_subsequence(a)
    print(length)
    print(moves)

solve()