def solve():
    k = int(input())
    
    digit_count = 0
    num_length = 1
    num = 1
    
    while digit_count + num_length * (num + 1 - 10**(num_length-1)) <= k:
        digit_count += num_length * (num + 1 - 10**(num_length-1))
        num_length += 1
        num = 10**(num_length-1)
        
    remaining = k - digit_count
    
    index_within_num = (remaining - 1) // num_length
    digit_index = (remaining - 1) % num_length
    
    target_num = num + index_within_num
    
    result = str(target_num)[digit_index]
    
    print(result)

solve()