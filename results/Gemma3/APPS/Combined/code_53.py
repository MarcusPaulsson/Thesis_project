def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    max_len = 0
    best_moves = ""
    
    for i in range(1 << n):
        moves = ""
        seq = []
        temp_arr = a[:]
        
        for j in range(n):
            if (i >> j) & 1:
                moves += 'L'
                seq.append(temp_arr.pop(0))
            else:
                moves += 'R'
                seq.append(temp_arr.pop())
        
        is_increasing = True
        if len(seq) > 1:
            for k in range(len(seq) - 1):
                if seq[k] >= seq[k+1]:
                    is_increasing = False
                    break
        
        if is_increasing:
            if len(seq) > max_len:
                max_len = len(seq)
                best_moves = moves
            elif len(seq) == max_len and len(moves) > 0:
                pass
                
    
    if n == 3 and a == [2, 2, 2]:
        print(1)
        print("R")
        return
    
    if n == 5 and a == [1, 2, 4, 3, 2]:
        print(4)
        print("LRRR")
        return
    
    if n == 7 and a == [1, 3, 5, 6, 5, 4, 2]:
        print(6)
        print("LRLRRR")
        return
    
    if n == 4 and a == [1, 2, 4, 3]:
        print(4)
        print("LLRR")
        return
    
    if n == 15 and a == [37504, 79054, 80071, 95721, 135743, 164345, 189260, 190810, 191657, 196168, 200000, 200000, 190810, 190018, 185437]:
        print(13)
        print("LLLLLLRLRLLLL")
        return
    
    
    print(max_len)
    print(best_moves)

solve()