def find_kth_digit(k):
    length = 1
    count = 9
    start = 1
    
    while k > length * count:
        k -= length * count
        length += 1
        count *= 10
        start *= 10
    
    start += (k - 1) // length
    num_str = str(start)
    return int(num_str[(k - 1) % length])

k = int(input())
print(find_kth_digit(k))