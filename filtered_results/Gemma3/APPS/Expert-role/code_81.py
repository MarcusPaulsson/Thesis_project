def solve():
    n = int(input())
    strings = []
    for _ in range(n):
        strings.append(input())
    
    def is_substring(s1, s2):
        return s1 in s2
    
    def check_order(arr):
        for i in range(len(arr)):
            for j in range(i):
                if not is_substring(arr[j], arr[i]):
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