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
            if any(f[0] == str(i + 1) for f in examples) or any(f[0] == str(i + 1) for f in regular):
                temp_name = generate_temp_name(files)
                moves.append(f"move {examples[i][0]} {temp_name}")
                
                # Find the file that needs to be moved to i+1
                target_file = ""
                for j in range(n):
                    if files[j][0] == str(i+1):
                        target_file = files[j][0]
                        break
                
                moves.append(f"move {target_file} {str(i + 1)}")
                moves.append(f"move {temp_name} {examples[i][0]}")
            else:
                moves.append(f"move {examples[i][0]} {str(i + 1)}")

    # Move regular tests to e+1, e+2, ..., n
    for i in range(len(regular)):
        if regular[i][0] != str(e + i + 1):
            if any(f[0] == str(e + i + 1) for f in examples) or any(f[0] == str(e + i + 1) for f in regular):
                temp_name = generate_temp_name(files)
                moves.append(f"move {regular[i][0]} {temp_name}")
                
                # Find the file that needs to be moved to e+i+1
                target_file = ""
                for j in range(n):
                    if files[j][0] == str(e+i+1):
                        target_file = files[j][0]
                        break
                
                moves.append(f"move {target_file} {str(e + i + 1)}")
                moves.append(f"move {temp_name} {regular[i][0]}")
            else:
                moves.append(f"move {regular[i][0]} {str(e + i + 1)}")

    print(len(moves))
    for move in moves:
        print(move)

def generate_temp_name(files):
    temp_name = "temp"
    i = 0
    while any(f[0] == temp_name + str(i) for f in files):
        i += 1
    return temp_name + str(i)

solve()