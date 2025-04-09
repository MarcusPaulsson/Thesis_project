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
            if any(files[j][0] == str(i + 1) for j in range(n)):
                # Need to move the existing file at i+1 to a temp location
                temp_name = generate_temp_name(files)
                moves.append(f"move {i+1} {temp_name}")
                files[next(j for j in range(n) if files[j][0] == str(i+1))][0] = temp_name
                
                moves.append(f"move {examples[i][0]} {i+1}")
                files[examples[i][1]][0] = str(i+1)
            else:
                moves.append(f"move {examples[i][0]} {i+1}")
                files[examples[i][1]][0] = str(i + 1)

    # Move regular to e+1, e+2, ..., n
    for i in range(len(regular)):
        if regular[i][0] != str(e + i + 1):
            if any(files[j][0] == str(e+i+1) for j in range(n)):
                temp_name = generate_temp_name(files)
                moves.append(f"move {e+i+1} {temp_name}")
                files[next(j for j in range(n) if files[j][0] == str(e+i+1))][0] = temp_name
                
                moves.append(f"move {regular[i][0]} {e+i+1}")
                files[regular[i][1]][0] = str(e + i + 1)
            else:
                moves.append(f"move {regular[i][0]} {e+i+1}")
                files[regular[i][1]][0] = str(e + i + 1)


    print(len(moves))
    for move in moves:
        print(move)

def generate_temp_name(files):
    temp_name = "temp00"
    i = 0
    while any(files[j][0] == temp_name + str(i) for j in range(len(files))):
        i += 1
    return temp_name + str(i)


solve()