def solve():
    n, pos, l, r = map(int, input().split())
    
    if l <= pos <= r:
        left_count = 0
        for i in range(1, pos):
            if not (l <= i <= r):
                left_count += 1
        
        right_count = 0
        for i in range(pos + 1, n + 1):
            if not (l <= i <= r):
                right_count += 1
        
        if left_count == 0 and right_count == 0:
            print(0)
            return
        
        if left_count == 0:
            print(right_count)
            return
        
        if right_count == 0:
            print(left_count)
            return
        
        print(min(left_count, right_count) + abs(left_count - right_count))
        return
    
    else:
        
        if pos < l:
            
            left_count = pos - 1
            right_count = n - r
            
            print(left_count + right_count)
            return
        else:
            
            left_count = l - 1
            right_count = n - pos
            
            print(left_count + right_count)
            return