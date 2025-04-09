def solve():
    x = int(input())

    def digit_sum(n):
        s = 0
        while n:
            s += n % 10
            n //= 10
        return s

    best_num = x
    max_sum = digit_sum(x)

    s = str(x)
    n = len(s)

    for i in range(n):
        if s[i] == '0':
            continue

        num_str = s[:i] + str(int(s[i]) - 1) + '9' * (n - i - 1)
        num = int(num_str)

        if num > 0 and num <= x:
           current_sum = digit_sum(num)
           if current_sum > max_sum:
               max_sum = current_sum
               best_num = num
           elif current_sum == max_sum and num > best_num:
               best_num = num

    print(best_num)

solve()