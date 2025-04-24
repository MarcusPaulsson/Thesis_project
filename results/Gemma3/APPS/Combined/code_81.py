def solve():
    n = int(input())
    strings = []
    for _ in range(n):
        strings.append(input())
    
    def is_substring(s1, s2):
        return s1 in s2
    
    def check_order(arr):
        for i in range(1, len(arr)):
            if not is_substring(arr[i], arr[i-1]):
                return False
        return True
    
    import itertools
    
    for perm in itertools.permutations(strings):
        if check_order(list(perm)):
            print("YES")
            for s in perm:
                print(s)
            return
    
    print("NO")

solve()