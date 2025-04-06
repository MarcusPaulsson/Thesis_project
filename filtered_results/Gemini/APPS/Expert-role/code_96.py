def solve():
    n = int(input())
    q = list(map(int, input().split()))
    
    def check_permutation(arr):
        if len(arr) != n:
            return False
        seen = set()
        for x in arr:
            if not (1 <= x <= n):
                return False
            if x in seen:
                return False
            seen.add(x)
        return True

    for first_element in range(1, n + 1):
        p = [first_element]
        valid = True
        for i in range(n - 1):
            next_element = p[-1] + q[i]
            p.append(next_element)
            
        if check_permutation(p):
          print(*p)
          return
    
    print(-1)


solve()