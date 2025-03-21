def solve():
    n = int(input())
    words = []
    for _ in range(n):
        words.append(input())

    def check(reversed_indices):
        modified_words = []
        for i in range(n):
            if i in reversed_indices:
                modified_words.append(words[i][::-1])
            else:
                modified_words.append(words[i])
        
        if len(set(modified_words)) != n:
            return False
        
        def can_arrange(arr):
            if not arr:
                return True
            
            import itertools
            for perm in itertools.permutations(arr):
                valid = True
                for i in range(len(perm) - 1):
                    if perm[i][-1] != perm[i+1][0]:
                        valid = False
                        break
                if valid:
                    return True
            return False
        
        return can_arrange(modified_words)

    for num_reversed in range(n + 1):
        for reversed_indices in itertools.combinations(range(n), num_reversed):
            if check(set(reversed_indices)):
                print(num_reversed)
                if num_reversed > 0:
                    print(*(x + 1 for x in reversed_indices))
                return

    print(-1)

import itertools

t = int(input())
for _ in range(t):
    solve()