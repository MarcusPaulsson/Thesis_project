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

    def find_index(filename):
        for i in range(n):
            if files[i][0] == filename:
                return i
        return -1

    def generate_temp_name(base):
        temp_name = base
        while find_index(temp_name) != -1:
            temp_name += "x"
        return temp_name

    # Move examples to 1, 2, ..., e
    for i in range(e):
        expected_name = str(i + 1)
        if examples[i][0] != expected_name:
            current_index = examples[i][1]
            
            target_index = find_index(expected_name)
            
            if target_index != -1:
                # Swap with a temporary file
                temp_name = generate_temp_name("temp")
                moves.append(f"move {expected_name} {temp_name}")
                moves.append(f"move {files[current_index][0]} {expected_name}")
                moves.append(f"move {temp_name} {examples[i][0]}")

                files[current_index][0] = expected_name
                files[target_index][0] = examples[i][0]
            else:
                moves.append(f"move {files[current_index][0]} {expected_name}")
                files[current_index][0] = expected_name

    # Move regular tests to e+1, e+2, ..., n
    for i in range(len(regular)):
        expected_name = str(e + i + 1)
        if regular[i][0] != expected_name:
            current_index = regular[i][1]
            
            target_index = find_index(expected_name)
            
            if target_index != -1:
                # Swap with a temporary file
                temp_name = generate_temp_name("temp")
                moves.append(f"move {expected_name} {temp_name}")
                moves.append(f"move {files[current_index][0]} {expected_name}")
                moves.append(f"move {temp_name} {regular[i][0]}")

                files[current_index][0] = expected_name
                files[target_index][0] = regular[i][0]
            else:
                moves.append(f"move {files[current_index][0]} {expected_name}")
                files[current_index][0] = expected_name

    print(len(moves))
    for move in moves:
        print(move)

solve()