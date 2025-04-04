def find_kth_digit(k):
    length = 0
    digits = 1
    while length + digits * 9 * 10**(digits-1) < k:
        length += digits * 9 * 10**(digits-1)
        digits += 1
    k -= length
    number = 10**(digits-1) + (k-1)//digits
    return str(number)[(k-1)%digits]

k = int(input())
print(find_kth_digit(k))