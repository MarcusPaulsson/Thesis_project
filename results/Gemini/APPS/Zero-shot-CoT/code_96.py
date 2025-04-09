def solve():
    n = int(input())
    q = list(map(int, input().split()))

    for first_element in range(1, n + 1):
        p = [first_element]
        valid = True
        for i in range(n - 1):
            next_element = p[-1] + q[i]
            p.append(next_element)
            if next_element < 1 or next_element > n:
                valid = False
                break

        if valid:
            seen = set()
            is_permutation = True
            for x in p:
                if x in seen:
                    is_permutation = False
                    break
                seen.add(x)
                if x < 1 or x > n:
                    is_permutation = False
                    break
            
            if is_permutation:
                print(*p)
                return
    
    print("-1")

solve()