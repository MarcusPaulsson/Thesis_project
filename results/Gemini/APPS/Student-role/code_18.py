def solve():
    s = input()
    n = len(s)
    t = []
    u = []
    
    def move1():
        nonlocal s, t
        if len(s) > 0:
            t.append(s[0])
            s = s[1:]
            return True
        return False
    
    def move2():
        nonlocal t, u
        if len(t) > 0:
            u.append(t[-1])
            t.pop()
            return True
        return False
    
    def find_min_suffix(arr):
        n = len(arr)
        min_suffix = [''] * n
        min_suffix[n-1] = arr[n-1]
        for i in range(n-2, -1, -1):
            min_suffix[i] = min(arr[i], min_suffix[i+1])
        return min_suffix
    
    min_suffixes = find_min_suffix(list(s))
    
    i = 0
    while len(s) > 0 or len(t) > 0:
        if len(s) > 0:
            if len(t) == 0:
                move1()
            elif min_suffixes[0] < t[-1]:
                move1()
            else:
                move2()
        else:
            move2()
            
    print("".join(u))

solve()