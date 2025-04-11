def is_stack_sortable(n, k, p):
    stack = []
    result = p[:]
    used = set(p)
    next_number = n

    for i in range(k):
        while stack and stack[-1] == next_number:
            result.append(stack.pop())
            next_number -= 1

        if p[i] > next_number:
            return -1

        stack.append(p[i])
        next_number = p[i] - 1

    while next_number > 0:
        if next_number not in used:
            result.append(next_number)
        else:
            while stack and stack[-1] == next_number:
                result.append(stack.pop())
        next_number -= 1

    while stack:
        result.append(stack.pop())

    return result

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))

    result = is_stack_sortable(n, k, p)

    if result == -1:
        print(-1)
    else:
        print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()