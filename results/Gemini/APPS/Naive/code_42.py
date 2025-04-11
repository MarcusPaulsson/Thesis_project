def solve():
    n = int(input())
    s = input()
    
    count = 0
    distinct_strings = set()
    
    for i in range(2**n):
        binary_string = bin(i)[2:].zfill(n)
        
        if binary_string in distinct_strings:
            continue
        
        is_substring = False
        for j in range(n):
            shifted_string = binary_string[j:] + binary_string[:j]
            if s in shifted_string:
                is_substring = True
                break
        
        if is_substring:
            count += 1
            
            # Add all cyclical shifts to the set to avoid duplicates
            for j in range(n):
                shifted_string = binary_string[j:] + binary_string[:j]
                distinct_strings.add(shifted_string)
    
    print(count)

solve()