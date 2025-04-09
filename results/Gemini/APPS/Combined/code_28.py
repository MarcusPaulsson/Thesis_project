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
    num_examples = len(examples)

    def find_unused_name(files):
        temp_name = "temp"
        temp_idx = 0
        while True:
            temp_file_name = temp_name + str(temp_idx)
            is_used = False
            for file in files:
                if file[0] == temp_file_name:
                    is_used = True
                    break
            if not is_used:
                return temp_file_name
            temp_idx += 1

    def move_file(source, destination):
        moves.append(f"move {source} {destination}")

    for i in range(num_examples):
        expected_name = str(i + 1)
        if examples[i][0] != expected_name:
            temp_name = find_unused_name(files)
            move_file(examples[i][0], temp_name)
            
            target_index = -1
            for j in range(n):
                if files[j][0] == expected_name:
                    target_index = j
                    break
            
            if target_index != -1:
                move_file(expected_name, examples[i][0])
            else:
                
                file_index = examples[i][1]
                files[file_index][0] = temp_name
                for j in range(len(examples)):
                    if examples[j][1] == file_index:
                        examples[j] = (temp_name, file_index)
                for j in range(len(regular)):
                    if regular[j][1] == file_index:
                        regular[j] = (temp_name, file_index)
            
            move_file(temp_name, expected_name)

    for i in range(len(regular)):
        expected_name = str(num_examples + i + 1)
        if regular[i][0] != expected_name:
            temp_name = find_unused_name(files)
            move_file(regular[i][0], temp_name)

            target_index = -1
            for j in range(n):
                if files[j][0] == expected_name:
                    target_index = j
                    break
            
            if target_index != -1:
                move_file(expected_name, regular[i][0])
            else:
                file_index = regular[i][1]
                files[file_index][0] = temp_name
                for j in range(len(examples)):
                    if examples[j][1] == file_index:
                        examples[j] = (temp_name, file_index)
                for j in range(len(regular)):
                    if regular[j][1] == file_index:
                        regular[j] = (temp_name, file_index)

            move_file(temp_name, expected_name)

    print(len(moves))
    for move in moves:
        print(move)

solve()