def solve():
    n = int(input())
    s = input()
    len_s = len(s)
    
    count = 0
    
    for i in range(2**n):
        binary_string = bin(i)[2:].zfill(n)
        
        is_substring = False
        for j in range(n):
            shifted_string = binary_string[j:] + binary_string[:j]
            if s in shifted_string:
                is_substring = True
                break
        
        if is_substring:
            count += 1
    
    print(count)

solve()