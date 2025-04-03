def solve():
    n = int(input())
    q = list(map(int, input().split()))

    def check_permutation(p):
        if len(p) != n:
            return False
        if len(set(p)) != n:
            return False
        for x in p:
            if x < 1 or x > n:
                return False
        return True

    def generate_permutation(first_element):
        p = [first_element]
        for i in range(n - 1):
            p.append(p[-1] + q[i])
        
        if check_permutation(p):
            return p
        else:
            return None

    for first_element in range(1, n + 1):
        permutation = generate_permutation(first_element)
        if permutation:
            print(*permutation)
            return
    
    print(-1)

solve()