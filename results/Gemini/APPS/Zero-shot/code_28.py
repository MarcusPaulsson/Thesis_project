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
    
    # Move examples to 1, 2, ..., e
    for i in range(e):
        if examples[i][0] != str(i + 1):
            moves.append((examples[i][0], str(i + 1)))
    
    # Move regular to e+1, e+2, ..., n
    for i in range(len(regular)):
        if regular[i][0] != str(e + i + 1):
            moves.append((regular[i][0], str(e + i + 1)))

    
    conflicts = set()
    for i in range(1, n + 1):
        conflicts.add(str(i))
    
    temp_moves = []
    
    for i in range(len(moves)):
        if moves[i][1] in conflicts:
            temp_name = generate_temp_name(files)
            temp_moves.append((moves[i][0], temp_name))
            moves[i] = (temp_name, moves[i][1])
            files.append([temp_name, 'temp'])
            
    
    final_moves = []
    for move in temp_moves:
        final_moves.append(move)
    for move in moves:
        final_moves.append(move)
    
    print(len(final_moves))
    for move in final_moves:
        print("move", move[0], move[1])

def generate_temp_name(files):
    existing_names = set()
    for file in files:
        existing_names.add(file[0])
    
    i = 0
    while True:
        temp_name = "temp" + str(i)
        if temp_name not in existing_names:
            return temp_name
        i += 1

solve()