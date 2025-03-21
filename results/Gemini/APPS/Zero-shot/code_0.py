def solve():
    n = int(input())
    words = []
    for _ in range(n):
        words.append(input())

    def reverse_word(word):
        return word[::-1]

    def check(reversed_indices):
        temp_words = []
        for i in range(n):
            if i in reversed_indices:
                temp_words.append(reverse_word(words[i]))
            else:
                temp_words.append(words[i])
        
        if len(set(temp_words)) != n:
            return False
        
        def can_be_arranged(arr):
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

        return can_be_arranged(temp_words)
    

    min_reversed = float('inf')
    best_reversed_indices = []

    for i in range(1 << n):
        reversed_indices = []
        for j in range(n):
            if (i >> j) & 1:
                reversed_indices.append(j)

        if check(reversed_indices):
            if len(reversed_indices) < min_reversed:
                min_reversed = len(reversed_indices)
                best_reversed_indices = reversed_indices

    if min_reversed == float('inf'):
        print("-1")
    else:
        print(min_reversed)
        if min_reversed > 0:
            print(*(x + 1 for x in best_reversed_indices))

t = int(input())
for _ in range(t):
    solve()