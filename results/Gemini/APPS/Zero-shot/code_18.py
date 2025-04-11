def solve():
    s = input()
    n = len(s)
    
    u = ""
    t = ""
    
    def move1():
        nonlocal s, t
        if len(s) > 0:
            t += s[0]
            s = s[1:]
            return True
        return False
    
    def move2():
        nonlocal t, u
        if len(t) > 0:
            u += t[-1]
            t = t[:-1]
            return True
        return False

    suffix_mins = [""] * (n + 1)
    suffix_mins[n] = ""
    
    for i in range(n - 1, -1, -1):
        if suffix_mins[i+1] == "" or s[i] <= suffix_mins[i+1][0]:
            suffix_mins[i] = s[i]
            if suffix_mins[i+1] != "":
              suffix_mins[i] += suffix_mins[i+1]
        else:
            suffix_mins[i] = s[i] + suffix_mins[i+1]
            suffix_mins[i] = min(suffix_mins[i], suffix_mins[i+1])
        
    
    suffix_min_chars = [""] * n

    min_char = 'z'
    for i in range(n):
        min_char = min(min_char, s[i])
        suffix_min_chars[i] = min_char
    
    curr_index = 0
    while curr_index < n:
        if len(t) > 0 and t[-1] <= suffix_min_chars[curr_index]:
            u += t[-1]
            t = t[:-1]
        else:
            t += s[0]
            s = s[1:]
            curr_index += 1

    while len(t) > 0:
        u += t[-1]
        t = t[:-1]
    
    print(u)

solve()