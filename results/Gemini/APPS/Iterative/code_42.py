def solve():
    n = int(input())
    s = input()
    len_s = len(s)
    
    count = 0
    distinct_strings = set()
    
    for i in range(2**n):
        binary_string = bin(i)[2:].zfill(n)
        
        is_substring = False
        for j in range(n):
            shifted_string = binary_string[j:] + binary_string[:j]
            if s in shifted_string:
                is_substring = True
                break
        
        if is_substring:
            if binary_string not in distinct_strings:
                count += 1
                distinct_strings.add(binary_string)
    
    print(count)

solve()