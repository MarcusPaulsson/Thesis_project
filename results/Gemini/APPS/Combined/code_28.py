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
    temp_files = set()

    def generate_temp_name():
        i = 1
        while True:
            temp_name = f"temp{i}"
            if temp_name not in [f[0] for f in files] and temp_name not in temp_files:
                return temp_name
            i += 1

    # Move examples to 1, 2, ..., e
    for i in range(len(examples)):
        if examples[i][0] != str(i + 1):
            target_name = str(i + 1)
            if any(f[0] == target_name for f in files):
                temp_name = generate_temp_name()
                moves.append(f"move {target_name} {temp_name}")
                temp_files.add(temp_name)
                
            moves.append(f"move {examples[i][0]} {target_name}")
            files[examples[i][1]][0] = target_name

    # Move regular tests to e+1, e+2, ..., n
    e = len(examples)
    for i in range(len(regular)):
        if regular[i][0] != str(e + i + 1):
            target_name = str(e + i + 1)
            if any(f[0] == target_name for f in files):
                temp_name = generate_temp_name()
                moves.append(f"move {target_name} {temp_name}")
                temp_files.add(temp_name)
                
            moves.append(f"move {regular[i][0]} {target_name}")
            files[regular[i][1]][0] = target_name

    print(len(moves))
    for move in moves:
        print(move)

solve()