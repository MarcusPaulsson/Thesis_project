def solve():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    max_beauty = 0
    for i in range(1 << n):
        temp_a = a[:]
        start = -1
        end = -1
        
        subarray_indices = []
        
        current_subarray = []
        
        bits = bin(i)[2:].zfill(n)
        
        is_in_subarray = False
        
        for j in range(n):
            if bits[j] == '1':
                if not is_in_subarray:
                    start = j
                    is_in_subarray = True
                end = j
            else:
                if is_in_subarray:
                    is_in_subarray = False
        
        if start != -1:
            for j in range(start, end + 1):
                temp_a[j] *= x
        
        current_beauty = 0
        max_so_far = 0
        
        for val in temp_a:
            current_beauty += val
            if current_beauty < 0:
                current_beauty = 0
            max_so_far = max(max_so_far, current_beauty)
        
        max_beauty = max(max_beauty, max_so_far)
    
    print(max_beauty)

solve()