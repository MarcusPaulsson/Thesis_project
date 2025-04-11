def solve():
    n = int(input())
    s = input()
    
    def contains(t, s):
        for i in range(len(t)):
            shifted_t = t[i:] + t[:i]
            if s in shifted_t:
                return True
        return False
    
    count = 0
    seen = set()
    for i in range(2**n):
        binary_string = bin(i)[2:].zfill(n)
        if contains(binary_string, s):
            if binary_string not in seen:
                count += 1
                seen.add(binary_string)
    
    print(count)

solve()