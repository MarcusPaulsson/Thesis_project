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

    e = len(examples)
    
    moves = []
    
    # Create a temporary mapping to avoid conflicts
    temp_names = [str(1000000 + i) for i in range(n)]

    # Move examples to temp names
    for i in range(e):
        if examples[i][0] != str(i + 1):
            moves.append(("move", examples[i][0], temp_names[examples[i][1]]))

    # Move regular tests to temp names
    for i in range(len(regular)):
        if regular[i][0] != str(e + i + 1):
            moves.append(("move", regular[i][0], temp_names[regular[i][1]]))

    # Move examples to correct positions
    for i in range(e):
        if examples[i][0] != str(i + 1):
            moves.append(("move", temp_names[examples[i][1]], str(i + 1)))

    # Move regular tests to correct positions
    for i in range(len(regular)):
        if regular[i][0] != str(e + i + 1):
            moves.append(("move", temp_names[regular[i][1]], str(e + i + 1)))

    print(len(moves))
    for move in moves:
        print(move[0], move[1], move[2])

solve()