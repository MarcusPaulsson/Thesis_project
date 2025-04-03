def max_digit_sum(x):
    x = str(x)
    n = len(x)
    max_sum = sum(map(int, x))
    max_num = int(x)
    
    for i in range(1, 10**n):
        num = str(i)
        if len(num) > n:
            break
        if num.count('0') > 0:
            continue
        digit_sum = sum(map(int, num))
        if digit_sum > max_sum or (digit_sum == max_sum and int(num) > max_num):
            max_sum = digit_sum
            max_num = int(num)
    
    return max_num

x = int(input())
print(max_digit_sum(x))