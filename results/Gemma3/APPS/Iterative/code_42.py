def solve():
    n = int(input())
    s = input()
    
    count = 0
    distinct_strings = set()
    
    for i in range(2**n):
        t = bin(i)[2:].zfill(n)
        
        found = False
        for j in range(n):
            shifted_t = t[j:] + t[:j]
            if s in shifted_t:
                found = True
                break
        
        if found:
            if t not in distinct_strings:
                count += 1
                distinct_strings.add(t)
    
    print(count)

solve()