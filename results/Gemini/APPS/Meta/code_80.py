def solve():
    n = int(input())
    s = input()
    
    def check(k):
        colors = [0] * n
        
        def can_sort(coloring):
            arr = list(s)
            
            for _ in range(n * (n - 1) // 2):
                swapped = False
                for i in range(n - 1):
                    if arr[i] > arr[i+1] and coloring[i] != coloring[i+1]:
                        arr[i], arr[i+1] = arr[i+1], arr[i]
                        swapped = True
                if not swapped:
                    break
            
            return "".join(arr) == "".join(sorted(s))

        
        import itertools
        
        for coloring in itertools.product(range(1, k + 1), repeat=n):
            if can_sort(coloring):
                return True, list(coloring)
        return False, None

    for k in range(1, n + 1):
        possible, coloring = check(k)
        if possible:
            print(k)
            print(*coloring)
            return

solve()