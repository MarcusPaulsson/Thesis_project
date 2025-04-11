def solve():
    k = int(input())
    
    digit_count = 0
    num = 1
    
    while digit_count < k:
        num_str = str(num)
        num_digits = len(num_str)
        
        if digit_count + num_digits >= k:
            index_within_num = k - digit_count - 1
            print(int(num_str[index_within_num]))
            return
        
        digit_count += num_digits
        num += 1

solve()