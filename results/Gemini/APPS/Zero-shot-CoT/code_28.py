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
            if str(i + 1) in [f[0] for f in examples] or str(i + 1) in [f[0] for f in regular]:
                # Need a temporary move
                temp_name = "temp"
                while temp_name in [f[0] for f in examples] or temp_name in [f[0] for f in regular]:
                    temp_name = ''.join(chr(ord('a') + (i % 26)) for i in range(6))
                moves.append(f"move {examples[i][0]} {temp_name}")
                moves.append(f"move {str(i + 1)} {examples[i][0]}")
                moves.append(f"move {temp_name} {str(i + 1)}")
            else:
                moves.append(f"move {examples[i][0]} {str(i + 1)}")

    # Move regular tests to e+1, e+2, ..., n
    for i in range(len(regular)):
        if regular[i][0] != str(e + i + 1):
            if str(e + i + 1) in [f[0] for f in examples] or str(e + i + 1) in [f[0] for f in regular]:
                # Need a temporary move
                temp_name = "temp"
                while temp_name in [f[0] for f in examples] or temp_name in [f[0] for f in regular]:
                    temp_name = ''.join(chr(ord('a') + (i % 26)) for i in range(6))
                moves.append(f"move {regular[i][0]} {temp_name}")
                moves.append(f"move {str(e + i + 1)} {regular[i][0]}")
                moves.append(f"move {temp_name} {str(e + i + 1)}")
            else:
                moves.append(f"move {regular[i][0]} {str(e + i + 1)}")

    print(len(moves))
    for move in moves:
        print(move)

solve()