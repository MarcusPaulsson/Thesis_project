def solve():
    k = int(input())
    
    digit_count = 0
    num = 1
    
    while digit_count < k:
        num_str = str(num)
        num_len = len(num_str)
        
        if digit_count + num_len <= k:
            digit_count += num_len
            num += 1
        else:
            index = k - digit_count - 1
            print(int(num_str[index]))
            return
    
solve()