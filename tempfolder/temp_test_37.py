def good_permutations(n):
    if n == 1:
        return [[1]]
    
    perms = good_permutations(n - 1)
    result = []

    for perm in perms:
        for i in range(n):
            new_perm = perm[:i] + [n] + perm[i:]
            result.append(new_perm)
    
    return result

def find_kth_good_permutation(n, k):
    good_perms = good_permutations(n)
    good_perms.sort()
    
    if k > len(good_perms):
        return -1
    
    return good_perms[k - 1]

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    t = int(data[0])
    results = []
    
    for i in range(1, t + 1):
        n, k = map(int, data[i].split())
        result = find_kth_good_permutation(n, k)
        if result == -1:
            results.append("-1")
        else:
            results.append(" ".join(map(str, result)))
    
    print("\n".join(results))

if __name__ == "__main__":
    main()