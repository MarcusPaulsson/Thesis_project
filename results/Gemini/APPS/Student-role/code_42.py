def solve():
    n = int(input())
    s = input()
    
    count = 0
    distinct_cyclical_strings = set()
    
    for i in range(2**n):
        binary_string = bin(i)[2:].zfill(n)
        
        is_substring = False
        for j in range(n):
            rotated_string = binary_string[j:] + binary_string[:j]
            if s in rotated_string:
                is_substring = True
                break
        
        if is_substring and binary_string not in distinct_cyclical_strings:
            count += 1
            distinct_cyclical_strings.add(binary_string)
            
    print(count)

solve()