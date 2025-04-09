def is_stack_sortable(arr):
    stack = []
    b = []
    
    for x in arr:
        stack.append(x)
        while stack and (not b or stack[-1] > b[-1]):
            b.append(stack.pop())

    return all(b[i] < b[i+1] for i in range(len(b) - 1)) if b else True

def solve():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))

    used = [False] * (n + 1)
    for x in p:
        used[x] = True

    remaining = []
    for i in range(n, 0, -1):
        if not used[i]:
            remaining.append(i)
    
    p_full = p + remaining

    if is_stack_sortable(p_full):
      print(*p_full)
      return

    import itertools
    
    best_permutation = None

    for permutation in itertools.permutations(remaining):
        current_permutation = p + list(permutation)
        if is_stack_sortable(current_permutation):
            if best_permutation is None:
                best_permutation = current_permutation
            else:
                if current_permutation > best_permutation:
                    best_permutation = current_permutation

    if best_permutation is None:
      print("-1")
    else:
      print(*best_permutation)

solve()