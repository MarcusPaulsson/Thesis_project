def solve():
    n = int(input())
    files = []
    for _ in range(n):
        files.append(input().split())

    examples = []
    regular = []
    for i in range(n):
        if files[i][1] == '1':
            examples.append((files[i][0], i))
        else:
            regular.append((files[i][0], i))

    moves = []
    e = len(examples)

    # Move examples to 1, 2, ..., e
    for i in range(e):
        if examples[i][0] != str(i + 1):
            moves.append(("move", examples[i][0], str(i + 1)))

    # Move regular tests to e+1, e+2, ..., n
    for i in range(len(regular)):
        if regular[i][0] != str(e + i + 1):
            moves.append(("move", regular[i][0], str(e + i + 1)))

    # Resolve conflicts using temporary names
    conflicts = {}
    for i in range(e):
        if examples[i][0] != str(i + 1):
            conflicts[str(i + 1)] = examples[i][0]
    for i in range(len(regular)):
        if regular[i][0] != str(e + i + 1):
            conflicts[str(e + i + 1)] = regular[i][0]

    temp_names = []
    for i in range(n + 1, n + 1 + len(conflicts)):
        temp_names.append(str(i))

    conflict_moves = []
    conflict_map = {}
    k = 0
    for target, original in conflicts.items():
        conflict_map[target] = temp_names[k]
        conflict_moves.append(("move", target, temp_names[k]))
        k += 1

    final_moves = []
    for move_type, file1, file2 in moves:
        if file2 in conflict_map:
            final_moves.append(("move", file1, conflict_map[file2]))
        else:
            final_moves.append(("move", file1, file2))

    for move_type, file1, file2 in conflict_moves:
        final_moves.insert(0, ("move", file1, file2))

    print(len(final_moves))
    for move_type, file1, file2 in final_moves:
        print(move_type, file1, file2)

solve()