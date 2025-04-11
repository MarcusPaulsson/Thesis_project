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

    temp_names = []
    for i in range(n):
        temp_name = f"temp{i}"
        while temp_name in [f[0] for f in files]:
            temp_name = f"temp{i+n}"
        temp_names.append(temp_name)

    
    def find_temp_name(existing_names):
        i = 0
        while True:
            temp_name = f"temp{i}"
            if temp_name not in existing_names:
                return temp_name
            i += 1

    
    existing_names = [f[0] for f in files]
    
    
    for i in range(e):
        if examples[i][0] != str(i + 1):
            if str(i + 1) in existing_names:
                temp_name = find_temp_name(existing_names)
                moves.append(f"move {str(i + 1)} {temp_name}")
                moves.append(f"move {examples[i][0]} {i + 1}")
                moves.append(f"move {temp_name} {examples[i][0]}")
                existing_names.remove(str(i+1))
                existing_names.append(str(i+1))
                existing_names.remove(examples[i][0])
                existing_names.append(str(i+1))
                
            else:
                moves.append(f"move {examples[i][0]} {i + 1}")
                existing_names.remove(examples[i][0])
                existing_names.append(str(i+1))

    for i in range(len(regular)):
        if regular[i][0] != str(e + i + 1):
            if str(e + i + 1) in existing_names:
                temp_name = find_temp_name(existing_names)
                moves.append(f"move {str(e + i + 1)} {temp_name}")
                moves.append(f"move {regular[i][0]} {e + i + 1}")
                moves.append(f"move {temp_name} {regular[i][0]}")
                existing_names.remove(str(e+i+1))
                existing_names.append(str(e+i+1))
                existing_names.remove(regular[i][0])
                existing_names.append(str(e+i+1))
            else:
                moves.append(f"move {regular[i][0]} {e + i + 1}")
                existing_names.remove(regular[i][0])
                existing_names.append(str(e+i+1))

    print(len(moves))
    for move in moves:
        print(move)

solve()