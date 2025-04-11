def solve():
    n = int(input())
    s = input()
    t = input()

    def check(res, s, t):
        for i in range(len(res) - 1):
            sub = res[i:i+2]
            if sub == s or sub == t:
                return False
        return True

    import itertools
    
    chars = ['a', 'b', 'c']
    
    possible_strings = []
    
    
    counts = {'a': n, 'b': n, 'c': n}
    
    def generate_strings(current_string, remaining_counts):
        if len(current_string) == 3 * n:
            possible_strings.append(current_string)
            return
        
        for char in chars:
            if remaining_counts[char] > 0:
                new_counts = remaining_counts.copy()
                new_counts[char] -= 1
                generate_strings(current_string + char, new_counts)
    
    
    generate_strings("", counts)
    
    for res in possible_strings:
        if check(res, s, t):
            print("YES")
            print(res)
            return
    
    print("NO")

solve()