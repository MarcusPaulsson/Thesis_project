def min_moves_to_divisible_by_25(n):
    n = str(n)
    length = len(n)
    if '00' in n or '25' in n or '50' in n or '75' in n:
        return 0
    if '0' in n:
        return length - n.rfind('0') - 1
    if '5' in n:
        return length - n.rfind('5') - 1
    return -1

n = int(input())
print(min_moves_to_divisible_by_25(n))