def solve():
    n = int(input())
    s = input()
    t = input()

    chars = ['a', 'b', 'c']

    import itertools

    for perm in itertools.permutations(chars):
        base_string = ""
        for i in range(n):
            base_string += perm[0]
        for i in range(n):
            base_string += perm[1]
        for i in range(n):
            base_string += perm[2]

        if s not in base_string and t not in base_string:
            print("YES")
            print(base_string)
            return
            
    for perm in itertools.permutations(chars):
        base_string = ""
        for i in range(n):
            base_string += perm[0]
        for i in range(n):
            base_string += perm[2]
        for i in range(n):
            base_string += perm[1]

        if s not in base_string and t not in base_string:
            print("YES")
            print(base_string)
            return

    print("NO")

solve()